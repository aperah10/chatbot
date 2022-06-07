from flask import Flask,request
from googlesearch import search
import requests
from twilio.twiml.messaging_response import MessagingResponse
from fastapi import FastAPI 

app =FastAPI()

@app.get("/")
async def hello():
    return "welcome page"
# app = Flask(__name__)

# @app.route("/")
# def hello():
#     return "Hello, World!"

# @app.route("/cht", methods=['POST'])
@app.post("/cht")
async def bot(user_msg):
    """Respond to incoming calls with a simple text message."""
    
    # Fetch the message
    
    bot_resp= MessagingResponse()
    msg = bot_resp.message()
    
    
    msg.body("Are you a Corn Grower ? \n yes \n no")

    # user_msg = request.form.get('Body').lower()
        
    if 'yes' in user_msg:
            msg.body("Did You Know that Fortenza Duo can secure your plant stand ?")
            msg.body("\n 1. if  you want to manage early season pests")
            msg.body("\n 2. if  you want to have excellent establishment")
            msg.body("\n 3. if  you want better yields")

            if '1' in user_msg:
                msg.body("videos1")
            if '2' in user_msg:
                msg.body("videos2")
            if '3' in user_msg:
                msg.body("videos3") 
    
    elif 'no' in user_msg:
            msg.body("Do you a Grow any other crop ?")
            msg.body("Yes")
            msg.body("No") 

    msg.body("Do you want to purchase FD ? \n yes \n no") 

            

   


    return str(bot_resp)
    # return user_msg

if __name__ == "__main__":
    # app.run(debug=True)
    app.run()
