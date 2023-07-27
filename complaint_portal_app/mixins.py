import random
from django.core.mail import send_mail
import random
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
# from twilio.rest import Client
import requests
import phonenumbers
from phonenumbers import parse
from phonenumbers import carrier, geocoder

# import os


def generate_otp():
    return str(random.randint(100000, 999999))


def send_otp_email(username, otp):
    # otp = str(random.randint(100000, 999999))
    subject = 'OTP Verification'
    message = f'Your OTP: {otp}'

# Redirect to OTP verification page
# return redirect('otp_verification')
    sender_email = 'shamshad.alam@rentokil-pci.com'
    recipient_email = username

    send_mail(subject, message, sender_email, [recipient_email])

def verify_mobile_number(phone_number):
    try:
        # Parse the phone number
        parsed_number = phonenumbers.parse(phone_number, "IN")

        # Check if the number is valid
        if not phonenumbers.is_valid_number(parsed_number):
            return False

        # Get the carrier information
        carrier_info = carrier.name_for_number(parsed_number, "en")
        print("Carrier: ", carrier_info)

        # Get the geolocation information
        region = geocoder.description_for_number(parsed_number, "en")
        print("Region: ", region)

        return True
    except phonenumbers.NumberParseException:
        return False

def send_otp_on_mobile_no(mobile_number, otp):
    # client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
    # message = client.messages.create(
    #     body=f"Your OTP is: {otp}",
    #     from_=settings.TWILIO_PHONE_NUMBER,
    #     to=mobile_number
    # )
    url=f"https://2factor.in/API/V1/{settings.API_KEY}/SMS/{mobile_number}/{otp}"
    response=requests.get(url)
    # account_sid = os.environ['TWILIO_ACCOUNT_SID']


    # auth_token = os.environ['TWILIO_AUTH_TOKEN']
    # client = Client(account_sid, auth_token)

    # message = client.messages 
    #                 .create(
    #                     body=f"Your OTP is: {otp}",
    #                     from_='+15017122661',
    #                     to='+15558675310'
    #                 )

# print(message.sid)

