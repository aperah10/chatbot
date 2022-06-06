from flask import Flask,request
from googlesearch import search
import requests
from twilio.twiml.messaging_response import MessagingResponse
  
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/cht", methods=['POST'])
def bot():
    """Respond to incoming calls with a simple text message."""
    # Fetch the message
    user_msg = request.form.get('Body')

    
    bot_resp= MessagingResponse()
    msg = bot_resp.message()
    if 'hello' in user_msg:
        msg.body("Hi there! How may I help you?")
    else:
        msg.body("Valid Question for this ")


    return str(bot_resp)

if __name__ == "__main__":
    # app.run(debug=True)
    app.run()
