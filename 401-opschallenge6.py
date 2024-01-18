#!/usr/bin/env python3

# importing necessary libraries

from cryptography.fernet import Fernet
import os

# creating a new fernet key

def key_write():
    key = Fernet.generate_key()
    with open ("key.key", "wb") as key_file:
        key_file.write(key)

def key_load():
    return open("key.key", "rb").read()

# encrypt file function

def encrypt_file(filename, key):
    # initialization fernet key
    f = Fernet(key)

    # open the file as read and store filename contents into file_data
    with open (filename, "rb") as file:
        file_data = file.read()
    # take file_data and writes a new file with file_data as contents
    ciphertext = f.encrypt(file_data)
    with open (filename, "wb") as encrypted_data:
        encrypted_data.write(ciphertext)
# function that decrypts the file
def decrypt_file(encrypted_file, key):
    # intiializing fernet key
    f = Fernet(key)
    with open (encrypted_file, "rb") as file:
        encrypted_data = file.read()

    # proceed to decrypt the data
    file_data = f.decrypt(encrypted_data)
    with open (encrypted_file, "wb") as decrypted_file:
        decrypted_file.write(file_data)


# function that encrypts the clear text
def encrypt_message(message, key):
    # initialize fernet key
    f = Fernet(key)
    encrypted_message = f.encrypt(message.encode())
    print(encrypted_message.decode())

# function to decrypt to clear text

def decrypt_message(encrypted_message, key):
    f = Fernet(key)
    message = f.decrypt(encrypted_message.encode())
    print(message.decode())

# function that encrypts recursively
def encrypt_path(path, key):
    f = Fernet(key)
    for root, dirs, files in os.walk(path):
        for file in files:
            file_path = os.path.join(root, file)
            if file_path.endswith(".txt"):
                encrypt_file(file_path, key)

def decrypt_path(path, key):
    f = Fernet(key)
    for root, dirs, files in os.walk(path):
        for file in files:
            path = os.path.join(root, file)
            if path.endswith(".txt"):
                decrypt_file(path, key)
# main code

# ask user what they would like to do
if not os.path.isfile("key.key"):
    key_write()
    key = key_load()
else:
    key = key_load()

decision = input("Pick what you want to do\n 1. encrypt a file\n 2. decrypt a file\n 3. encrypt a message\n 4. decrypt a message\n 5. Encrypt an entire folder\n 6. Decrypt an entire folder\n")

if decision == "1":
    filename = input("Please enter a file you want to encrypt\n")
    encrypt_file(filename, key)
if decision == "2":
    encrypted_file = input("Please enteer a file you would like to decrypt\n")
    decrypt_file(encrypted_file, key)
if decision == "3":
    message = input("Please enter a message you would like to encrypt\n")
    encrypt_message(message, key)
if decision == "4":
    encrypted_message = input("Please enter an encrypted message you would like to decrypt\n")
    decrypt_message(encrypted_message, key)
if decision == "5":
    path = input("Please enter the folder name you would like to encrypt\n")
    encrypt_path(path, key)
if decision == "6":
    path = input("Please enter the encrypted folder name\n")
    decrypt_path(path, key)
else:
    print("Invalid option")