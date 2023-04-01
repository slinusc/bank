import json


class CurrencyValidation:

    def __init__(self):
        self.file = 'current_exchange_rates.json'
        self.valid_currencies = self.get_valid_currencies()

    def get_valid_currencies(self):
        with open(self.file, 'r') as f:
            data = json.load(f)
            valid_currencies = list(data['rates'].keys())  # Holen Sie sich die Währungscodes aus dem 'rates' Feld
        return valid_currencies

    def check_valid_currencies(self, currency):
        if currency in self.valid_currencies:
            return True
        else:
            return False


if __name__ == '__main__':

    # Erstellen einer Instanz von CurrencyValidation
    currency_validation = CurrencyValidation()

    # Printen aller validen Währungskürzels
    print(currency_validation.valid_currencies)

    # Test der Methode check_valid_currencies
    print(currency_validation.check_valid_currencies('CHF'))
    print(currency_validation.check_valid_currencies('XYZ'))
