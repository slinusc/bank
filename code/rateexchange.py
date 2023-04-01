import os
import json
import datetime as dt
import requests


class RateExchange:
    def __init__(self, base_currency='CHF'):
        self.base_currency = base_currency
        self.file = 'current_exchange_rates.json'
        self.url = f'https://open.er-api.com/v6/latest/{base_currency}'

    def get_exchange_rate(self, to_curr):
        if not os.path.exists(self.file):
            last_request = dt.date(year=1, month=1, day=1)
        else:
            with open(self.file, 'r') as f:
                data = json.load(f)
                last_request = dt.datetime.strptime(data['last_request'], "%Y-%m-%d").date()

        if (dt.datetime.today().date() - last_request).days >= 1:
            self.cache_exchange_rates()
            with open(self.file, 'r') as f:
                data = json.load(f)

        return data['last_request'], data['rates'][to_curr]

    def cache_exchange_rates(self):
        response = requests.request("GET", self.url)
        if response.status_code == 200:
            data = response.json()
            current_rates = data['rates']
            last_request = dt.datetime.today().date().strftime("%Y-%m-%d")
            to_save = {"last_request": last_request, "rates": current_rates}

            with open(self.file, 'w') as f:
                json.dump(to_save, f)

            return dt.datetime.strptime(last_request, "%Y-%m-%d").date()
        else:
            raise ValueError(f"Error fetching exchange rates: {response.status_code}")


if __name__ == "__main__":

    # Erstellen einer Instanz der RateExchange Klasse
    exchange = RateExchange()

    # Cache wird automatisch beschrieben bzw. abgerufen, wenn letztes Update >= 1 Tag
    date, rate = exchange.get_exchange_rate("USD")
    print(f'{date}: 1 CHF = {rate} USD')