from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import wikipedia

app = Flask(__name__)


@app.route('/sms', methods=['POST'])
def sms():

    # Recieves body of request
    message_body = request.form['Body']

    # Create a Twilio response object to be able to send the answer back
    resp = MessagingResponse()

    # Compile message to be sent
    reply_text = get_reply(message_body)

    # Text back our response!
    resp.message(reply_text)
    return str(resp)

def get_reply(message):

    # Turn message into lowercase to allow lowercase entries
    message = message.lower().split()

    # Retrieve url for wikipedia page if no exists
    # If not , return a string stating otherwise
    try:
        page = wikipedia.page(message)
        get_url = page.url

        answer = "A Wikipedia article was found matching your entry: " + get_url
    except:
        answer = "No article found matching your entry. I'm sorry!"

    return answer

if __name__ == '__main__':
    app.run()