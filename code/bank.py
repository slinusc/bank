import savingaccount as sa
import youthaccount as ya
import rateexchange as re
import mockpersongenerator as mpg
import bankclient as bc
import person as pn
import currencyvalidation as cv


class Bank:
    def __init__(self):
        self.clients = {}
        self.count_account = 1
        self.rate_exchange = re.RateExchange()
        self.currency_validator = cv.CurrencyValidation()

    def create_new_client(self, person: pn.Person):
        client = bc.BankClient(person, f'K-Nr-{len(self.clients) + 1}')
        client_key = client.client_id
        self.clients[client_key] = client
        return client_key

    def create_account(self, client_key: str, account_type: str, balance, currency='CHF'):
        client = self.clients[client_key]
        iban = f"CH93 0076 2011 6238 1237 {self.count_account}"

        if not self.currency_validator.check_valid_currencies(currency):
            raise ValueError(f"Invalid currency: {currency}")

        if account_type == 'youth':
            account = ya.YouthAccount(client.person, iban, balance, currency)
            client.add_account(account)
            self.count_account += 1
            return account.iban_number
        elif account_type == 'saving':
            account = sa.SavingAccount(client.person, iban, balance, currency)
            client.add_account(account)
            self.count_account += 1
            return account.iban_number

    def transaction(self, iban_from, iban_to, amount):
        withdrawal_success = False
        deposit_success = False
        from_account_currency = None
        to_account_currency = None

        for client_key in self.clients:
            for k in range(len(self.clients[client_key].accounts)):
                if self.clients[client_key].accounts[k].iban_number == iban_from:
                    from_account_currency = self.clients[client_key].accounts[k].currency
                elif self.clients[client_key].accounts[k].iban_number == iban_to:
                    to_account_currency = self.clients[client_key].accounts[k].currency

        if from_account_currency != 'CHF':
            date, exchange_rate = self.rate_exchange.get_exchange_rate(
                from_account_currency)
            amount = round(amount / exchange_rate, 2)

        if to_account_currency != 'CHF':
            date, exchange_rate = self.rate_exchange.get_exchange_rate(
                to_account_currency)
            amount = round(amount * exchange_rate, 2)

        for client_key in self.clients:
            for k in range(len(self.clients[client_key].accounts)):
                if self.clients[client_key].accounts[k].iban_number == iban_from:
                    withdrawal_success = self.clients[client_key].accounts[k].withdraw(amount)
                elif self.clients[client_key].accounts[k].iban_number == iban_to:
                    deposit_success = self.clients[client_key].accounts[k].deposit(amount)

        if withdrawal_success and deposit_success:
            print('Transaction successful! ')
            return True
        elif withdrawal_success and not deposit_success:
            # Rollback the withdrawal
            for client_key in self.clients:
                for j in range(len(self.clients[client_key].accounts)):
                    if self.clients[client_key].accounts[j].iban_number == iban_from:
                        self.clients[client_key].accounts[j].deposit(amount)
            raise ValueError("Transaction failed: Unable to deposit the amount.")
        else:
            raise ValueError("Transaction failed: Unable to withdraw the amount.")


if __name__ == '__main__':

    # Instanziieren einer Test-Bank
    test_bank = Bank()

    # Instanziieren zweier Test-Personen
    test_youth_person = mpg.mock_person_generator(1, 'youth')[0]
    test_saving_person = mpg.mock_person_generator(1, 'adult')[0]

    # Erstellen zweier Clients
    key_client1 = test_bank.create_new_client(test_youth_person)
    print(f'Kundennummer: {key_client1}')
    key_client2 = test_bank.create_new_client(test_saving_person)
    print(f'Kundennummer: {key_client2}')
    print()

    # Erstellen von Konten
    test_bank.create_account(key_client1, 'saving', 500, "USD")
    test_bank.create_account(key_client1, 'youth', 10000, "CHF")
    test_bank.create_account(key_client2, 'saving', 250000, "EUR")

    # printen aller Klienten in Kundenkartei inkl. der Währung und IBAN
    for i in test_bank.clients:
        print(f'Name: {test_bank.clients[i].person.name}')
        print(f'Kundennummer: {test_bank.clients[i].client_id}')
        print('Konten:')
        for k in range(len(test_bank.clients[i].accounts)):
            print(test_bank.clients[i].accounts[k].currency, '-', test_bank.clients[i].accounts[k].iban_number)
        print()

    # Test von Transaktionen mit Fremdwährungen
    print(f'from: {test_bank.clients[key_client2].person.name}, balance: {test_bank.clients[key_client2].accounts[0].balance}')
    print(f'to: {test_bank.clients[key_client1].person.name}, balance: {test_bank.clients[key_client1].accounts[0].balance}')
    print()
    test_bank.transaction('CH93 0076 2011 6238 1237 3', 'CH93 0076 2011 6238 1237 1', 200)
    print()
    print(f'{test_bank.clients[key_client2].person.name}, new balance: {test_bank.clients[key_client2].accounts[0].balance}')
    print(f'{test_bank.clients[key_client1].person.name}, new balance: {test_bank.clients[key_client1].accounts[0].balance}')

    # Test CurrencyValidation
    # test_bank.create_account(key_client2, 'saving', 250000, "EUGAJAR")
