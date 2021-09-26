from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()



def out_crypto(Btc):
    print(Btc['name']+" "+Btc['symbol'], "price:", Btc['current_price'], "$")


for i in range(1):
    b = int(input("Number to output top: "))
    list = cg.get_coins_markets("usd")[:b]
    for crypto in list:
        out_crypto(crypto)
