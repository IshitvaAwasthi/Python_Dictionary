# To recommend best match, take confirmation from user and optimize definitions
import json
import difflib
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(w):
    # To implement case sensitivity
    # To check if the word is the valid or not
    if w.lower() in data:
        return data[w]
    #For Proper Nouns
    elif w.title() in data:
        return data[w.title()]
    elif w.upper() in data:
        return data[w.upper()]
    elif len(get_close_matches(w, data.keys())) > 0:  # To recommend best match
        # To take confirmation from user
        yn = input("Did you mean {} instead? Enter Y if yes or N if no: ".format(get_close_matches(w, data.keys())[0]))  
        if yn == "Y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == "N":
            return "The word does not exist. Please check it."
        else:
            return "We didn't understand your entry."
    else:
        return "The word does not exist. Please check it."

word = input("Enter word: ")
output = translate(word)
# Optimizing the definition
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
