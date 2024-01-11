#!/usr/bin/env python3

# Importing libraries needed
import os
import datetime
import time
from ping3 import ping
from email.message import EmailMessage
import ssl
import smtplib

# asking for email address and password to be used as sender
email_address = input("Please enter an email address that you will use for notifications: ")
email_reciever = 'skalyx86@gmail.com'
password = input ("Please enter password for email address: ")
subject = "automated sensor update"
em = EmailMessage()
ts = datetime.datetime.now()

# Previous uptime_sensor from last lab 
def uptime_sensor(ping_target):
    # Seeing if the ping is successful
    success = ping(ping_target, timeout=1)

    # if success does not time out, create the status variable saying it was successful
    if success:
        status = "Up"
    
    # Else, the target cannot be pinged
    else:
        status = "Down"
    
    # Print out the time stamp, the status, and the IP address
    print(f"{ts} {status}: {ping_target}")
    time.sleep(2)
# Asking for IP to ping
ping_target = input("What IP would you like to ping? ")

# running function
uptime_sensor(ping_target)

success = ping(ping_target, timeout=1)
if success:
    status = "Up"
else:
    status = "Down"

body = "{ping_target} has changed to {status} at {ts}"


em['From'] = email_address
em['To'] = email_reciever
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_address, password)
    smtp.sendmail (email_address, email_reciever, em.as_string())