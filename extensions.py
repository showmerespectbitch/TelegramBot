import requests
import json


from config import keys


class APIException(Exception):
    pass


class Conversion:
    @staticmethod
    def get_price(base, quote, amount):
        try:
            if base.lower() not in keys.keys():
                raise APIException(f"Не нашёл такой валюты: {base}")
            elif quote.lower() not in keys.keys():
                raise APIException(f"Не нашёл такой валюты: {quote}")
            elif not amount.isnumeric():
                raise APIException(f"{amount} не похоже на количество!")
        except APIException as e:
            return e
        else:
            base = keys[base.lower()]
            quote = keys[quote.lower()]
            amount = float(amount)
            response = requests.get(f'https://api.exchangerate.host/convert?from={base}&to={quote}')
            data = json.loads(response.content)
            return round(data['info']['rate'] * amount, 2)