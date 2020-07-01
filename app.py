import requests
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse






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

    elif str(msg) in names_list:
        print(names_list)
        string_result = ''
        response = requests.get('https://api.exchangeratesapi.io/latest?base={}'.format(msg))
        result = response.json()
        for key,value in result['rates'].items():
            string_result = string_result + (key+ ' --> ' + str(value)) +'\n'

        resp.message(string_result)
        return str(resp)



    else:
        resp.message('You said: {}'.format(msg))
        return str(resp)






if __name__ == '__main__':
    app.run(debug=True)

