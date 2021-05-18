from requests import get

url = 'https://api.pro.coinbase.com'
products = '/products'

r = get(url=url+products)

pairs = [ x for x in r]

# {'id': 'ALGO-EUR', 'base_currency': 'ALGO', 'quote_currency': 'EUR', 'base_min_size': '1', 'base_max_size': '500000', 'quote_increment': '0.0001', 'base_increment': '1', 'display_name': 'ALGO/EUR',
#     'min_market_funds': '10', 'max_market_funds': '100000', 'margin_enabled': False, 'post_only': False, 'limit_only': False, 'cancel_only': False, 'trading_disabled': False, 'status': 'online', 'status_message': ''}
