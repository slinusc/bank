import mockpersongenerator as mpg


class BankClient:
    def __init__(self, person, client_id):
        self.client_id = client_id
        self.person = person
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)

    def __str__(self):
        return f'customer id: {self.client_id}, owner: {self.person}, accounts: {self.accounts}'


if __name__ == '__main__':
    test_person = mpg.mock_person_generator(1, 'adult')[0]
    test_bank_client = BankClient(test_person, 'XYZ')
    print(test_bank_client)