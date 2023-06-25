import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
ROCK
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
PAPER
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
SCISSORS
'''
game=[rock,paper,scissors]
user_input=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
player=game[user_input]
print(player)
game=[rock,paper,scissors]
computer_input=random.randint(0,2)
computer=game[computer_input]
print(computer)

if player==0 and computer==1:
    print("you lost")
elif computer==0 and player==1:
    print("you  won")
elif player==1 and computer==2:
    print("you lost")
elif computer==1 and player==2:
    print("you  won")
elif player==2 and computer==1:
    print("you lost")
elif computer==2 and player==1:
    print("you  won")

elif player==0 and computer==2:
    print("you lost")
elif computer==0 and player==2:
    print("you  won")


