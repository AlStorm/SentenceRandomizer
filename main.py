import random

#Function that manipulates the entire sentence.
def senManipul(sentence):
    sentence = sentence.lower()
    words = sentence.split()
    random.shuffle(words)
    words[0] = words[0].capitalize()
    finalString = " ".join(words)
    finalString += "."
    return finalString

final = print(senManipul(input(str("Input a sentence: "))))