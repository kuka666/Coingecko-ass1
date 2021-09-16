from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()


def sort_by_cap(e):
    return e['market_cap_rank']


def out_coin(Btc):
    print(Btc['symbol'], "price:", Btc['current_price'], "$")


for i in range(1):
    n = int(input("Number to output top: "))
    coin_list = cg.get_coins_markets("usd")[:n]
    coin_list.sort(key=sort_by_cap)
    for coin in coin_list:
        out_coin(coin)
