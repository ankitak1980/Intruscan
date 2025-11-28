from twilio.rest import Client

account_sid = ''
auth_token = ''
client = Client(account_sid, auth_token)
def sendSms():
    message = client.messages.create(
    from_='+12564149766',
    body='Alert',
    to=''
    )

    print(message.sid)