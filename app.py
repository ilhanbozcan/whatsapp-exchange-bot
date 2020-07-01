import requests
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse


url = 'https://prime.exchangerate-api.com/v5/642fb88fc669b5fa92814bd0/latest/TL'
response = requests.get(url)
data = response.json()

app = Flask(__name__)


@app.route('/', methods = ['GET'])
def hello():
    return 'Welcome'



@app.route('/sms', methods = ['POST'])
def sms_reply():
    msg = request.form.get('Body')

    if(msg=='dolar kuru'):

        resp = MessagingResponse()
        resp.message(data)
    else:
        resp = MessagingResponse()
        resp.message('You said: {}'.format(msg))


    return str(resp)



if __name__ == '__main__':
    app.run(debug=True)

