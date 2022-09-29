# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

myNumber = ''

def notify_call():
    call = client.calls.create(
                            twiml='<Response><Say>Hi Prashant, US Embassy at London, UK has opened the appointment for B2 VISA at London. \n'
                            'Please login immediately to book your appointment.</Say></Response>',
                            to=myNumber,
                            from_=''
                        )

def notify_text():
    message = client.messages.create(
                              body='Hi Prashant, Appointments are still not available. You will be notified through a call \n'
                              'as soon as the appointments are open.',
                              from_='',
                              to=myNumber
                          )

if __name__ == "__main__":
    notify_call()