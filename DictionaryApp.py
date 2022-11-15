import json
import difflib as d

data = json.load(open("076 data.json",'r'))

def def_word(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif len(d.get_close_matches(w,data.keys())) > 0:
        option = input("Did u mean {} instead ? Enter Y if Yes, N if No : ".format(d.get_close_matches(w,data.keys())[0]))
        option = option.upper()
        if option == 'Y':
            return data[d.get_close_matches(w,data.keys())[0]]
        else:
            return "We didn't understand your entry."
    else:
        return "The word doesn't exist. Please double check it."


word = input("Enter word : ")
define_word = def_word(word)
if type(define_word) is list:
    for i in define_word:
        print(i)
else:
    print(define_word)
