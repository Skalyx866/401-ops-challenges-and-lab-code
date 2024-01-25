#!/usr/bin/env python3 

# Script Name:                  Class 11
# Author:                       Cody Juhl
# Date of latest revision:      22 Jan 2024
# Purpose:                      TCP range scanner to see whether a port is accessible and a ICMP ping sweep


# importing necessary libraries
import scapy.all as scapy
from scapy.all import sr1, IP, TCP, send
import ipaddress

# creating variables to store ping sweep results and IP CIDR block

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

# function that sweeps the network for IPS
def ping_sweep():
    target = input("Please enter an IP e.g 10.0.0.0\n")


    # send ICMP to IP address

    response=sr1(IP(dst=str(target)) / scapy.ICMP(), timeout=1, verbose=0)

        # check to see if there is a response
    if response is None:
        print(f"{target} is down")

    elif int(response.getlayer(scapy.ICMP).type) == "3" and int(response.getlayer(scapy.ICMP).code in [1, 2, 3, 9, 10, 13]):
        print(f"{target} is filtering ICMP traffic")
        
    else:
        print(f"{target} is up!")
        print(f"Beginning port scan")
        port_scan(target)
    
# port scan function
def port_scan(host):
    port_range_in = input(f"Please enter a port range e.g 10-90\n")
    first_port, last_port = map(int, port_range_in.split("-"))
    port_range_out = range(first_port, last_port, +1)
    print(f"Scanning for open ports\n")
    for port in port_range_out:
        port_scanner(host, port)

    # main function
ping_sweep()