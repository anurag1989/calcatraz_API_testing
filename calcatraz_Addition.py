__author__ = 'Anurag'


import requests


class Calcatraz_Addition(object):
    def request(self, number1, number2):
        url = "http://www.calcatraz.com/calculator/api"
        response = requests.get(url, params={'c': str(number1) + '+' + str(number2)})
        # print response.url
        status = response.status_code
        responses=response.text
        print status
        print responses




