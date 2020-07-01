import requests
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse



exchange = {'EUR': 'Euro' ,'USD': 'US dollar', 'JPY': 'Japanese yen', 'BGN': 'Bulgarian lev', 'CZK': 'Czech koruna', 'DKK': 'Danish krone', 'GBP': 'Pound sterling', 'HUF': 'Hungarian forint', 'PLN': 'Polish zloty', 'RON': 'Romanian leu', 'SEK': 'Swedish krona', 'CHF': 'Swiss franc', 'ISK': 'Icelandic krona', 'NOK': 'Norwegian krone', 'HRK': 'Croatian kuna', 'RUB': 'Russian rouble', 'TRY': 'Turkish lira', 'AUD': 'Australian dollar', 'BRL': 'Brazilian real', 'CAD': 'Canadian dollar', 'CNY': 'Chinese yuan renminbi', 'HKD': 'Hong Kong dollar', 'IDR': 'Indonesian rupiah', 'ILS': 'Israeli shekel', 'INR': 'Indian rupee', 'KRW': 'South Korean won', 'MXN': 'Mexican peso', 'MYR': 'Malaysian ringgit', 'NZD': 'New Zealand dollar', 'PHP': 'Philippine peso', 'SGD': 'Singapore dollar', 'THB': 'Thai baht', 'ZAR': 'South African rand'}



app = Flask(__name__)


@app.route('/', methods = ['GET'])
def hello():
    return 'Welcome'



@app.route('/sms', methods = ['POST'])
def sms_reply():
    response = requests.get('https://api.exchangeratesapi.io/latest?base=USD')
    names = ""
    names_list =[]
    for i in response.json()['rates'].keys():
            names_list.append(i)

    msg = request.form.get('Body')
    resp = MessagingResponse()

    if(msg=='Birimler'):

        count = 0
        for i in response.json()['rates'].keys():
            names_list.append(i)
            names = names+'   ' + i

            if count == 5:
                names = names + '\n'
                count = 0
            count+=1

        resp.message(names)
        return str(resp)

    elif str(msg) in exchange.keys():
        print()

        string_result = ''
        response = requests.get('https://api.exchangeratesapi.io/latest?base={}'.format(msg))
        result = response.json()
        for key,value in result['rates'].items():
            string_result = string_result + (key+ ' --> ' + str(exchange.get(key)) + '-->' + str(value)) +'\n'

        resp.message(string_result)
        return str(resp)



    else:
        resp.message('You said: {}'.format(msg))
        return str(resp)






if __name__ == '__main__':
    app.run(debug=True)

