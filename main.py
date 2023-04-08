import time

from pybit.usdt_perpetual import HTTP

from keys import api_key, api_secret


def main():
    session = HTTP(
        api_key=api_key,
        api_secret=api_secret,
    )

    old_btc = None
    old_eth = None
    dif_price_btc = None
    dif_price_eth = None

    while True:
        symbols_info = session.latest_information_for_symbol()
        for symbol in symbols_info['result']:
            if symbol['symbol'] == 'BTCUSDT':
                new_btc_price = symbol['last_price']
                if old_btc:
                    dif_price_btc = round((float(new_btc_price) * 100 / float(old_btc)) - 100, 2)
                old_btc = new_btc_price

            elif symbol['symbol'] == 'ETHUSDT':
                new_eth_price = symbol['last_price']
                if old_eth:
                    dif_price_eth = round((float(new_eth_price) * 100 / float(old_eth)) - 100, 2)
                old_eth = new_eth_price

        if dif_price_btc and dif_price_eth:
            if (abs(dif_price_btc) - abs(dif_price_eth)) > 1:
                print('Изменения больше, чем на 1%')
        time.sleep(60 * 60)


if __name__ == '__main__':
    main()
