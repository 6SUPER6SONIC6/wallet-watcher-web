import requests
from django.conf import settings

from .utils import format_amount, is_spam_token


def get_wallet_data(address: str) -> list | None:
    try:
        result = requests.get(
            f"{settings.ETH_BASE_URL}getAddressInfo/{address}?apikey={settings.API_KEY}", )
    except requests.exceptions.RequestException as e:
        print(e)
        return None
    else:
        if result.status_code != 200:
            return None

        json_data = result.json()
        return parse_wallet(json_data)


def parse_wallet(json_data) -> list:
    tokens = []
    eth = json_data['ETH']
    eth_balance = eth['balance']
    eth_rate = eth['price']['rate']
    eth_usd_value = eth_balance * eth_rate

    tokens.append({
        'name': 'Ethereum',
        'symbol': 'ETH',
        'balance': format_amount(eth_balance),
        'usd_value': format_amount(eth_usd_value),
    })

    if json_data.get('tokens'):
        for token in json_data['tokens']:
            token_info = token['tokenInfo']
            if not is_spam_token(token_info):
                raw_balance = int(token['rawBalance'])
                decimals = int(token_info['decimals'])
                balance = raw_balance / (10 ** decimals)
                price = token_info['price']
                rate = float(price['rate'])
                usd_value = balance * rate
                icon_url = f""

                tokens.append({
                    'name': token_info['name'],
                    'symbol': token_info['symbol'],
                    'balance': format_amount(balance),
                    'usd_value': format_amount(usd_value),
                    'icon_url': icon_url,
                })

    return tokens