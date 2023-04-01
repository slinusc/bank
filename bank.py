import savingaccount as sa
import youthaccount as ya
import random as rm
import mockpersongenerator as mpg
import bankclient as bc
import person as pn

class Bank:
    def __init__(self):
        self.clients = {}

    def create_new_client(self, person: pn.Person):
        client = bc.BankClient(person, f'K-Nr-{len(self.clients) + 1}')
        client_key = client.customer_id
        self.clients[client_key] = client
        return client_key

    def create_account(self, client_key: str, account_type: str, balance, currency='CHF'):
        client = self.clients[client_key]
        account_number = f"CH93 0076 2011 6238 {str(rm.randint(1000, 9999))} 7"
        if account_type == 'youth':
            account = ya.YouthAccount(client.person, account_number, balance, currency)
            client.add_account(account)
            return account.iban_number
        elif account_type == 'saving':
            account = sa.SavingAccount(client.person, account_number, balance, currency)
            client.add_account(account)
            return account.iban_number


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
    test_bank.create_account(key_client1, 'youth', 100)
    test_bank.create_account(key_client1, 'saving', 10000)
    test_bank.create_account(key_client2, 'saving', 250000)

    # printen aller Klienten in Kundenkartei inkl. der Iban ihrer Konten
    for i in test_bank.clients:
        print(f'Name: {test_bank.clients[i].person.name}')
        print('Konten:')
        for k in range(len(test_bank.clients[i].accounts)):
            print(test_bank.clients[i].accounts[k].iban_number)
        print()