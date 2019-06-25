import logging, re
import requests

endpoint = 'https://api.sbif.cl/api-sbifv3/recursos_api'

class API():
    def __init__(self, key):
        self._api_key = key

    def __request_apisbif(self, url_endpoint):

        url_query_strings = {'apikey': self._api_key,
                             'formato': 'json'}

        response = requests.get(url_endpoint, params=url_query_strings)

        if not response.ok:
            print 'ERROR APISBIF Response: {}'.format(response.text)
            return response.json()
        
        return response.json()

    def get_uf(self, year='', month='', day=None):
        if day is not None:
            url_endpoint = endpoint + '/uf/{}/{}/dias/{}'.format(year, month, day)
        else:
            url_endpoint = '/uf/{}/{}'.format(year, month)
            url_endpoint = endpoint + re.sub(r'\/{2,}', '/', url_endpoint)

        return self.__request_apisbif(url_endpoint)
    
    def get_usd(self, year='', month='', day=None):
        if day is not None:
            url_endpoint = endpoint + '/dolar/{}/{}/dias/{}'.format(year, month, day)
        else:
            url_endpoint = '/dolar/{}/{}'.format(year, month)
            url_endpoint = endpoint + re.sub(r'\/{2,}', '/', url_endpoint)

        return self.__request_apisbif(url_endpoint)