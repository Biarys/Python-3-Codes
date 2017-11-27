import json
from difflib import get_close_matches

data = json.load(open("data.json",'r'))

def translate(word):
    if word in data:
        return data[word]

    elif word.title() in data:
        return data[word.title()]

    elif get_close_matches(word, data.keys(), cutoff=0.8):
        print("Did you mean {0} instead? Type yes to get the result for {0} or no otherwise".format(get_close_matches(word, data.keys())[0]))
        x = input().lower()

        while(x != 'yes' or x != 'no'):
            if x == "yes":
                return data[get_close_matches(word, data.keys())[0]]

            elif x == "no":
                return "Okay..."

            else:
                print("That wasn't yes or no! Try again!")
                x = input().lower()
    else:
        return "The word doesn't exist. Please double check it."

word = input("Enter word: ").lower()

output = translate(word)

if type(output) == list:
    num = 1
    for item in output:
        print("{}) ".format(num) + item)
        num += 1
else:
    print(output)
