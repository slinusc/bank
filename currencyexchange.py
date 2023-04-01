import requests
import datetime as dt
import json
import os


def get_exchange_rates(to_curr):

    if not os.path.exists('current_exchange_rates.json'):
        last_request = dt.date(year=1, month=1, day=1)
    else:
        with open('current_exchange_rates.json', 'r') as f:
            data = json.load(f)
            last_request = dt.datetime.strptime(data['last_request'], "%Y-%m-%d").date()

    if (dt.datetime.today().date() - last_request).days >= 1:
        cache_exchange_rates()
        with open('current_exchange_rates.json', 'r') as f:
            data = json.load(f)

    return data['rates'][to_curr]


def cache_exchange_rates(from_curr='CHF'):
    file = 'current_exchange_rates.json'
    url = f'https://open.er-api.com/v6/latest/{from_curr}'
    response = requests.request("GET", url)
    if response.status_code == 200:
        data = response.json()
        current_rates = data['rates']
        last_request = dt.datetime.today().date().strftime("%Y-%m-%d")
        to_save = {"last_request": last_request, "rates": current_rates}

        with open(file, 'w') as f:
            json.dump(to_save, f)

        return dt.datetime.strptime(last_request, "%Y-%m-%d").date()
    else:
        raise ValueError(f"Error fetching exchange rates: {response.status_code}")


if __name__ == "__main__":

    # Cache wird automatisch beschrieben bzw. abgerufen, wenn letztes Update >= 1 Tag
    print(f'1 CHF: {get_exchange_rates("USD")} USD')