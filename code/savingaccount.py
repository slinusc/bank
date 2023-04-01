import account as acc
import mockpersongenerator as mpg


class SavingAccount(acc.Account):
    account_type = 'saving'

    def __init__(self, client, iban_number, balance=0, currency='CHF'):
        super().__init__(iban_number, balance, currency)
        self.client = client
        self.interest_rate = 0.1

    def get_interest_rate(self):
        return self.interest_rate

    def set_interest_rate(self, new_rate):
        self.interest_rate = new_rate

    def withdraw(self, amount):
        if (self.balance - amount) < 0:
            self.balance -= amount * 1.02
        else:
            self.balance -= amount

    def __repr__(self):
        return f'account type: {self.account_type}, owner: {self.client.name}, age: {self.client.age}, ' \
               f'IBAN: {self.iban_number}, balance: {self.balance}, interest rate: {self.interest_rate},' \
               f' currency: {self.currency}'


if __name__ == '__main__':
    example_person = mpg.mock_person_generator(1, 'adult')[0]
    example_saving_account = SavingAccount(example_person, f"CH93 0076 2011 6238 6666 7")
    print(example_saving_account)
