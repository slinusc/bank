import account as ac
import mockpersongenerator as dc


class YouthAccount(ac.Account):
    monthly_withdraw = 2000
    account_type = 'youth'

    def __init__(self, client, iban_number, balance=0, currency='CHF'):
        super().__init__(iban_number, balance, currency)
        self.client = client
        self.balance = balance
        self.currency = currency

        if client.age <= 25:
            self.interest_rate = 2.0
        else:
            self.interest_rate = 0.1

    def withdraw(self, amount):
        if amount > YouthAccount.monthly_withdraw:
            raise ValueError('Bezug übersteigt monatliche Limite!')
        else:
            self.balance -= amount

    def set_interest_rate(self, new_rate):
        self.interest_rate = new_rate

    def __repr__(self):
        return f'account type: {self.account_type}, owner: {self.client.name}, IBAN: {self.iban_number}, ' \
               f'balance: {self.balance}, interest rate: {self.interest_rate},' \
               f' currency: {self.currency}, age: {self.client.age}'


if __name__ == '__main__':
    example_person = dc.mock_person_generator(1, 'youth')[0]
    example_youth_account = YouthAccount(example_person, f"CH93 0076 2011 6238 6666 7")
    print(example_youth_account)