import requests
from fixerio import Fixerio


response = requests.get('https://api.exchangeratesapi.io/latest?base=USD')
names = ""

result = response.json()
print(result)

string = ''

for key,value in result['rates'].items():
    string = string + (key+ ' --> ' + str(value)) +'\n'

print(string)








