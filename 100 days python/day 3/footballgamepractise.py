from tkinter import CENTER
from turtle import left, right


print('''                                                                    
   ad88                               88                     88 88  
  d8"                           ,d    88                     88 88  
  88                            88    88                     88 88  
MM88MMM ,adPPYba,   ,adPPYba, MM88MMM 88,dPPYba,  ,adPPYYba, 88 88  
  88   a8"     "8a a8"     "8a  88    88P'    "8a ""     `Y8 88 88  
  88   8b       d8 8b       d8  88    88       d8 ,adPPPPP88 88 88  
  88   "8a,   ,a8" "8a,   ,a8"  88,   88b,   ,a8" 88,    ,88 88 88  
  88    `"YbbdP"'   `"YbbdP"'   "Y888 8Y"Ybbd8"'  `"8bbdP"Y8 88 88  
                                                                    ''')
player=int(input("choose a player:1.aakif 2.talha 3.salman  4.riyaz"))
if(player==1):
    print("well experience  person in football good choice-->you have chosen aakif to shoot the penalty ")
    shoot=(input("where you want to shoot left right centre "))
    shoot1=shoot.lower()
    if(shoot1=="right"):
        print("goal")
    else:
        print("great save by the goally")
if(player==2):
    print("well experience  person in football good choice:you have chosen Talha the chaddi to shoot the penalty ")
    shoot=(input("where you want to shoot left right centre "))
    shoot1=shoot.lower()
    if(shoot1=="centre"):
        print("goal")
    else:
        print("great save by the goally")
if(player==3):
    print("well experience  person in football good choice:you have chosen salman rancho to shoot the penalty ")
    shoot=(input("where you want to shoot left right centre "))
    shoot1=shoot.lower()
    if(shoot1=="left"):
        print("goal")
    else:
        print("great save by the goally")
if(player==4):
    print("well experience  person in football good choice:you have chosen aakif to shoot the penalty ")
    shoot=(input("where you want to shoot left right centre "))
    shoot1=shoot.lower()
    if(shoot1==left):
        print("goal")
    else:
        print("great save by the goally")

        
if(player==4):
    print("well experience  person in football good choice:you have chosen riyaz don to shoot the penalty ")
    shoot=(input("where you want to shoot left right centre "))
    shoot1=shoot.lower()
    if(shoot1=="right"):
        print("goal")
    else:
        print("great save by the goally")

        




