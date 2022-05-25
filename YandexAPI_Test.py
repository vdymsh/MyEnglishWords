"""
Request syntax
https://translate.yandex.net/api/v1.5/tr.json/translate
 ? key=<API key>
 & text=<text to translate>
 & lang=<translation direction>     # en-ru
 & [format=<text format>]           # plain (default) / html
 & [options=<translation options>]  # has default may be omitted
 & [callback=<name of the callback function>]   
 # May by omitted - The name of the callback function. Use for getting a JSONP response.
 """
import requests

URL = "https://translate.yandex.net/api/v1.5/tr.json/translate"
KEY = "trnsl.1.1.20200218T073727Z.d6b80c77761af4f2.2c8367f00446617f28c66ac134d6761db3797750"


def translate_me(my_text):
    request_params = {
        "key": KEY,
        "text": my_text,
        "lang": 'en-ru'
    }
    response = requests.get(URL, params=request_params)
    return response.json()


json = translate_me('Estimate')
print(json)
# print(' '.join(json['text']))
