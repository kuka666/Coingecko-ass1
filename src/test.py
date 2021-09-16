from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()


def print_coin(Btc):
    print(Btc['symbol'], "price:", Btc['current_price'], "$")


def cap_sort(e):
    return e['market_cap_rank']


for i in range(1):
    n = int(input("Number to output top: "))
    coin_list = cg.get_coins_markets("usd")[:n]
    coin_list.sort(key=cap_sort)
    for coin in coin_list:
        print_coin(coin)
