import requests


def request_bom_data(bom_url, max_tries=10):
    response = None
    while response is None or response.status_code != 200 or max_tries >= 0:
        try:
            response = requests.get(bom_url)
            if response.status_code == 200:
                break
        except requests.exceptions.RequestException:
            pass
        max_tries -= 1
    return response.json()


if __name__ == "__main__":

    # Request an URL
    bom_data = request_bom_data('http://160.85.252.148')

    for i in bom_data:
        print(f'{i}: {bom_data[i]}')
