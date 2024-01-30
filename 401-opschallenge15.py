# Script Name:                  Class 16
# Author:                       Cody Juhl
# Date of latest revision:      1/29/2024
# Purpose:                      Python script that prompts the user for a wordlist and starts a brute force attack

import ssl
import nltk
from nltk.corpus import words

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context


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

decision= input(f'Please choose a mode\n 1. Offensive\m 2. Defensive\n')

if decision == "1":
    load_wordlist()

elif decision == "2":
    list = get_list()
    check_word(list)
else:
    print(f"Invalid option")