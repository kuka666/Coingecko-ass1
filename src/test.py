from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()


def crypto_sort(a):
    return a['market_cap_rank']


def out_crypto(Btc):
    print(Btc['symbol'], "price:", Btc['current_price'], "$")


for i in range(1):
    b = int(input("Number to output top: "))
    list = cg.get_coins_markets("usd")[:b]
    list.sort(key=crypto_sort)
    for crypto in list:
        out_crypto(crypto)
