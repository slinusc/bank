import re


def validate_swiss_iban(iban):
    # Entfernen von Leerzeichen aus der IBAN
    iban = iban.replace(" ", "")

    # Überprüfen, ob die IBAN mit CH beginnt
    if not iban.startswith("CH"):
        return False

    # Überprüfen der Länge der IBAN
    if len(iban) != 21:
        return False

    # Überprüfen, ob die IBAN nur aus Zahlen und Buchstaben besteht
    if not re.match("^[a-zA-Z0-9]*$", iban[2:]):
        return False

    return True


class Account:
    def __init__(self, iban_number, balance, currency):
        self.currency = currency
        self.balance = balance

        #if validate_swiss_iban(iban):
        self.iban_number = iban_number
        #else:
        #    raise ValueError("Ungültige IBAN-Nummer")

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def get_balance(self):
        return self.balance

    def get_currency(self):
        return self.currency

    def __repr__(self):
        return f'IBAN: {self.iban_number}, balance: {self.balance},' f' currency: {self.currency}'


if __name__ == '__main__':
    test_account = Account(f"CH93 0076 2011 6238 1234 7", 111, 'USD')
    print(test_account)