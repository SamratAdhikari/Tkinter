# Dictionary

# Modules -------------------------------------------
import json

# load the data from data.json
data = json.load(open('data.json', 'r'))


# Function ------------------------------------------
def translate(word):
    meaning = ''
    word = word.lower()
    if word in data:
        for item in data[word]:
            meaning = meaning + str(item) + "\n"
        return meaning
    else:
        return "The meaning doesnt exist.\n"


# Program loop -------------------------------------

if __name__ == '__main__':
    while True:
        # ask for user input
        askWord = str(input("\nEnter the word: "))
        print(translate(askWord.lower()))

        askRun = input("Search again? (y/n) ")
        if askRun.lower() != "y":
            break
