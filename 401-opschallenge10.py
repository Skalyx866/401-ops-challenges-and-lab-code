#!/usr/bin/env python3 

# Script Name:                  Class 10
# Author:                       Cody Juhl
# Date of latest revision:      22 Jan 2024
# Purpose:                      TCP range scanner to see whether a port is accessible


# importing necessary libraries
import scapy.all as scapy
from scapy.all import sr1, IP, TCP, send

# creating function for port scanner

def port_scanner(host, port):

# setting the source port
    src_port = 22

    # initiate the three way handshake

    response = sr1(IP(dst=host) / TCP(sport=src_port, dport=port, flags="S"), timeout=1, verbose=0)

    # checking the response to see if you get something back or not

    if response is None:
        print(port + "is filtered or closed")

    elif response.haslayer(TCP):
        layer = response.getlayer(TCP)
        if layer.flags == 0x12:
            send(IP(dst=host) / TCP(sport=src_port, dport=port, flags="R"), verbose=0)
            print(f"{port} is currently open")
        elif layer.flags == 0x14:
            print("The port is current closed")
    else:
        print("Cannot determine state of port")
    
    # main function
target = "scanme.nmap.org"
portrange = range(22, 23)

    # Sends ping to test if computer is up

response = sr1(IP(dst=target) / scapy.ICMP(), verbose=0)

if response:
    response.show()
    
    # goes through the port range to see if they are open
    for ports in portrange:
        port_scanner(target, ports)