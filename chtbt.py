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
    bot_resp= MessagingResponse()
    msg = bot_resp.message()
    user_msg = request.form.get('Body').lower()
    
    msg.body("Are you a Corn Grower ?")
        
          
         
    if 'yes' or"Yes" in user_msg:
            msg.body("Did You Know that Fortenza Duo can secure your plant stand ?")
            msg.body("videos1")
            msg.body("videos2")
            msg.body("videos3")

            if 'videos1' in user_msg:
                msg.body("videos1")
    
    elif 'no' or"No" in user_msg:
            msg.body("Do you a Grow any other crop ?")
            msg.body("Yes")
            msg.body("No") 

            

   


    return str(bot_resp)

if __name__ == "__main__":
    # app.run(debug=True)
    app.run()
