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
    global ip_range
    global active_hosts

    hosts = list(ip_range)
    hosts.remove(ip_range.broadcast_address)
    hosts.remove(ip_range.network_address)

    # send ICMP to hosts in CIDR block
    for host in hosts:
        response=sr1(IP(dst=str(host)) / scapy.ICMP(), timeout=1, verbose=0)

        # check to see if there is a response
        if response is None:
            print(f"{host} is down")

        elif int(response.getlayer(scapy.ICMP).type) == "3" and int(response.getlayer(scapy.ICMP).code in [1, 2, 3, 9, 10, 13]):
            print(f"{host} is filtering ICMP traffic")
        
        else:
            print(f"{host} is up!")
            active_hosts+=1
    print(f"A total of {active_hosts} are up!")

    # main function

choice = input("What would you like to do?\n 1. Port Scanner\n 2. ICMP sweep\n 3. Exit\n")

if choice == "1":

    target = input("Please enter an IP address you would like to port scan\n")
    port_range_in = input("Please enter the range of ports you want to scan e.g 20-439\n")
    first_port, end_port = map(int, port_range_in.split("-"))
    port_range_out = range(first_port, end_port, +1)
    for port in port_range_out:
        port_scanner(target, port)
    
elif choice == "2":
    ip_block = input("Please enter an IP block in CIDR format e.g 10.0.0.0/24\n")
    ip_range = ipaddress.IPv4Network(ip_block)
    active_hosts = 0
    ping_sweep()

elif choice == "3":
    print(f"Exiting")

else:
    print(f"Invalid option")