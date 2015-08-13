__author__ = 'Anurag'


import requests


class Calcatraz_Addition(object):
    def request(self, number1, number2):
        url = "http://www.calcatraz.com/calculator/api"
        response = requests.get(url, params={'c': str(number1) + '+' + str(number2)})
        if response.status_code==200:
           output=response.content
           print output
           if output.strip(" ")=="answer":
              return "Not able to do addition"
           else:
               try:
                    return int(output.strip(" "))
               except ValueError:
                    return "Did'nt get any response from API"
        elif response.status_code==500:
            return "Found 500 internal server error"
        elif response.status_code==404:
            return "Found 404 Status code"





# c=Calcatraz_Addition()
# print c.request("%@","@#@#")