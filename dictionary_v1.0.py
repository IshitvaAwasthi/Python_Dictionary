#Checking for invalid word and case sensitivity
import json

data = json.load(open("data.json"))

def translate(w):
    if w in data:                                                # To check if the word is the valid or not
        w.lower()                                               # To implement case sensitivity                                             
        return data[w]
    #For Proper Nouns
    elif w.title() in data:
        return data[w.title()]
    else:
        return "The word does not exist. Please check it."

word = input("Enter word: ")
print(translate(word)) 

