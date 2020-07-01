import requests
from fixerio import Fixerio


response = requests.get('https://api.exchangeratesapi.io/latest?base=USD')
names = ""

count = 0
for i in response.json()['rates'].keys():

    names = names+'   ' + i

    if count == 5:
        names = names + '\n'
        count = 0
    count+=1

print(names)
#print(response.status_code)



