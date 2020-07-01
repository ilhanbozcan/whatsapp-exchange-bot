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
    msg = request.form.get('Body')

    if(msg=='Birimler'):

        resp = MessagingResponse()
        count = 0
        for i in response.json()['rates'].keys():
            names_list.append(i)
            names = names+'   ' + i

            if count == 5:
                names = names + '\n'
                count = 0
            count+=1


        return(resp.message(names))

    elif str(msg) in names_list:
        response = requests.get('https://api.exchangeratesapi.io/latest?base={}'.format(msg))
        resp = MessagingResponse()
        return(resp.message(response.json))








    else:
        resp = MessagingResponse()
        resp.message('You said: {}'.format(msg))
        return(resp.message())






if __name__ == '__main__':
    app.run(debug=True)

