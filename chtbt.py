from flask import Flask
from googlesearch import search
import requests
from twilio.twiml.messaging_response import MessagingResponse
  
  
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"


@app.route("/cht", methods=["GET"])
  
# chatbot logic
def bot():
  
    # user input
    user_msg = request.values.get('Body', '').lower()
  
    bot_resp= MessagingResponse()
    msg = bot_resp.message()

    if 'hello' in user_msg:
        msg.body("Hi there! How may I help you?")
    elif 'you r hero' in user_msg:
        msg.body("yes i m hero.")
        
    else:
        msg.body("hahahaha")
  
    
    return str(bot_resp)
  
  
if __name__ == "__main__":
    app.run(debug=True)