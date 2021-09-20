# CoinGecko API wrapper

Python3 wrapper around the [CoinGecko](https://www.coingecko.com/) API (V3)

### Installation

PyPI

```bash
pip install pycoingecko
```

or from source

```bash
git clone https://github.com/man-c/pycoingecko.git
cd pycoingecko
python3 setup.py install
```

### Usage

```python
from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()
```

### Examples
```python
cg.get_coins_markets("usd")

Number to output top: 5
btc price: 47654 $
eth price: 3574.42 $
ada price: 2.43 $
usdt price: 0.999801 $
bnb price: 424.69 $
```
