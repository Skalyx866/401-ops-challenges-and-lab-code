#!/usr/bin/env python3

# declaration of libraries imported
import time
import datetime
from ping3 import ping

# declare variable for future time stamp
ts = datetime.datetime.now()

# function that will carry out the execution
def uptime_sensor(ping_target):

    # Seeing if the ping is successful
    success = ping(ping_target, timeout=1)

    # if success does not time out, create the status variable saying it was successful
    if success:
        status = "Ping has reached intended target"
    
    # Else, the target cannot be pinged
    else:
        status = "Ping has failed"
    
    # Print out the time stamp, the status, and the IP address
    print(f"{ts} {status}: {ping_target}")
    time.sleep(2)

ping_target = input("Please enter an IP address ex: 8.8.8.8.8\n")
uptime_sensor(ping_target)
