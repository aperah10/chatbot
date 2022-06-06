from flask import Flask,request
from googlesearch import search
import requests
from twilio.twiml.messaging_response import MessagingResponse
  
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/cht", methods=['POST'])
def sms_reply():
    """Respond to incoming calls with a simple text message."""
    # Fetch the message
    msg = request.form.get('Body')

    # Create reply
    resp = MessagingResponse()
    resp.message("im rahul: {}".format(msg))

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)

# from flask import Flask,request
# from googlesearch import search
# import requests
# from twilio.twiml.messaging_response import MessagingResponse
  
  
# app = Flask(__name__)
  
# @app.route("/", methods=["POST"])
  
# # chatbot logic
# def bot():
  
#     # user input
#     user_msg = request.values.get('Body', '').lower()
  
#     # creating object of MessagingResponse
#     response = MessagingResponse()
  
#     # User Query
#     q = user_msg + "geeksforgeeks.org"
  
#     # list to store urls
#     result = []
  
#     # searching and storing urls
#     for i in search(q, tld='co.in', num=6, stop=6, pause=2):
#         result.append(i)
  
#     # displaying result
#     msg = response.message(f"--- Result for '{user_msg}' are  ---")
  
#     msg = response.message(result[0])
#     msg = response.message(result[1])
#     msg = response.message(result[2])
#     msg = response.message(result[3])
#     msg = response.message(result[4])
  
#     return str(response)
  
  
# if __name__ == "__main__":
#     app.run()