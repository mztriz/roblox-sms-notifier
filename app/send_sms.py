from twilio.rest import Client
import settings
import os

def send_sms(playerid, status):
    client = Client(os.getenv("twilio_sid"), os.getenv("twilio_token"))
    client.messages.create(to=os.getenv("twilio_tnum"),
                        from_=os.getenv("twilio_fnum"),
                        body=f"The player {playerid} is {status}!")
