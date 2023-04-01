class Account:
    def __init__(self, iban_number, balance, currency):
        self.currency = currency
        self.balance = balance
        self.iban_number = iban_number

    def deposit(self, amount):
        self.balance += amount
        return True

    def withdraw(self, amount):
        self.balance -= amount
        return True

    def get_balance(self):
        return self.balance

    def get_currency(self):
        return self.currency

    def __repr__(self):
        return f'IBAN: {self.iban_number}, balance: {self.balance},' f' currency: {self.currency}'


if __name__ == '__main__':
    test_account = Account(f"CH93 0076 2011 6238 1234 7", 111, 'USD')
    print(test_account)