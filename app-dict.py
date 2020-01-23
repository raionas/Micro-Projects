import json
import pyfiglet
from difflib import get_close_matches

banner = pyfiglet.figlet_format("Interactive Dictionary: version 1", font="bubble")
print(banner)

data = json.load(open("data.json"))

def translate(w):
    w = w.lower()
    isMatch = get_close_matches(w, data.keys())
    if w in data:
        return data[w]
    elif w.title() in data:
        return data[w.title()]
    elif w.upper() in data:
        return data[w.upper()]
    elif len(isMatch) > 0:
        answer = input(f"Did you mean {isMatch[0]} instead?\nEnter Y (yes) or N (no): ")
        if answer.lower() == 'y':
            return data[isMatch[0]]
        elif answer.lower() == 'n':
            return f"The word, {w} doesn't exist. Please double check it."
        else:
            return f"Your entry, {answer} was not understood."
    else:
        return f"The word you typed, '{w}' doesn't exist. Please triple check it."

if __name__ == '__main__':
    try:
        word = input("Enter a word: ")
        output = translate(word)

        if type(output) == list:
            for value in output:
                print(value)
        else:
            print(output)
    except SystemExit or KeyboardInterrupt:
        print("Terminating program.")
