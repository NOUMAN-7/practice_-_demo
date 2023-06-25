from tkinter import N


print("roller coaster")
height=int(input("enter the height in cm:"))
bill=0

if(height>=120):
    print("you can ride the roller coaster")
    age=int(input("enter you age:"))
    if(age<12):
        bill=5
        print("you have to pay $5")
    elif(age<=18):
        bill=7
        print("you have to pay $7")
    elif age >=45 and age<=55:
        print("free ride for aged person")
    else:
        bill=12
        print("you have to pay $12")
    photo=input("do you want to take photo Y or N:")
    if photo=="Y" or photo=="y":
        #add $3 to thier bill
        bill += 3
    print(f"your final bill payment is {bill}")
    
else:
    print("you cant ride roller coaster")
