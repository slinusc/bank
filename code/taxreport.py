import bank
import mockpersongenerator as mpg
import youthaccount as ya
import savingaccount as sa
import datetime as dt
import currencyexchange as ce


class TaxReport:
    def __init__(self, bank):
        self.bank = bank

    def generate(self):

        current_year = dt.datetime.now().year
        fiscal_year = current_year - 1

        for client_key, client in self.bank.clients.items():

            # Dict aller Accounts je Klient wird angelegt
            savings_accounts = {}
            youth_accounts = {}

            print(f"Tax report {current_year} for fiscal year {fiscal_year} for client {client_key}")
            print(f"Name: {client.person.name}")

            for account in client.accounts:
                # alle Währungen der Accounts werden überprüft und im Falle von Fremdwährungen in CHF umgerechnet
                if account.currency != 'CHF':
                    exchange_rate = ce.get_exchange_rate(account.currency)
                    print(f"Converting {account.currency} to CHF at the rate {exchange_rate}")

                if isinstance(account, ya.YouthAccount):
                    youth_accounts[account.iban_number] = account.balance * (exchange_rate if account.currency != 'CHF' else 1)
                elif isinstance(account, sa.SavingAccount):
                    savings_accounts[account.iban_number] = account.balance * (exchange_rate if account.currency != 'CHF' else 1)

            # die umgerechneten Kontoinformationen werden ausgegeben
            if savings_accounts:
                print("** Savings Accounts **")
                for iban, balance in savings_accounts.items():
                    print(f"{iban}: {balance:.2f} CHF")

            if youth_accounts:
                print("** Youth Accounts **")
                for iban, balance in youth_accounts.items():
                    print(f"{iban}: {balance:.2f} CHF")

            print()


if __name__ == '__main__':

    # Instanziieren einer Test-Bank
    test_bank = bank.Bank()

    # Instanziieren zweier Test-Personen
    test_youth_person = mpg.mock_person_generator(1, 'youth')[0]
    test_saving_person = mpg.mock_person_generator(1, 'adult')[0]

    # Erstellen zweier Clients
    key_client1 = test_bank.create_new_client(test_youth_person)
    key_client2 = test_bank.create_new_client(test_saving_person)

    # Erstellen von Konten in Fremdwährungen und CHF
    test_bank.create_account(key_client1, 'youth', 100, 'USD')
    test_bank.create_account(key_client1, 'saving', 10000)
    test_bank.create_account(key_client2, 'saving', 250000, 'JPY')
    test_bank.create_account(key_client2, 'saving', 222, 'GBP')

    # Erstellen der Instanz TaxReport
    tax_report = TaxReport(test_bank)

    # generieren der Steuerunterlagen inklusive aktuellem Wechselkurs
    tax_report.generate()
