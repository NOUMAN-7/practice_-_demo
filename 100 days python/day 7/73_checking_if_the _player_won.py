import random
words=["nouman","aakif","aasim"]
random_words=random.choice(words)
print(f"the random word we got-->{random_words}")
word_length=len(random_words)
display=[]
for _ in range (word_length):
    display+="_"



###user input with condition run untill the blanks is fully filled
endofthegame=False

#while not endofthegame:
#another method
while endofthegame==False:
    guess=input("enter the letter ").lower()
    for positon in range(word_length):
        letter=random_words[positon]
        if(letter==guess):
            display[positon]=letter
    print(display)
    if("_" not in display):
        endofthegame=True
        print("congratulations you have gussed the word")

