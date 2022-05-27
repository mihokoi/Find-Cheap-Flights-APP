from twilio.rest import Client

TWILIO_SID = "AC3c5b2e6562989d74a23878267ca5a670"
TWILIO_AUTH_TOKEN = "1e0ad803a4a99af583ac77baec1fe715"
TWILIO_VIRTUAL_NUMBER = "+12058584849"
TWILIO_VERIFIED_NUMBER = "+48666877772"

class NotificationManager:
    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER
        )
        print(message.sid)
