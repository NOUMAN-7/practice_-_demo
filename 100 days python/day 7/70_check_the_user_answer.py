import random
words=["nouman","aakif","aasim"]
random_words=random.choice(words)
#user input
guess=input("enter the letter ").lower()

for letter in random_words:
    if(letter==guess):
        print("right")
    else:
        print("wrong")
