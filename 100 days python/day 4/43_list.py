#list
#mistake mention quotient to intialiaze th values if you want to store string value
from ctypes.wintypes import PINT


fruits=["apple","mango","banana","jerry","watermelon"]
print("before changing")
print(fruits)
#accesing particular values\
print(fruits[0])

#we can use negative hwich will print from back word 
print(fruits[-1])
#changing the value using the index 
fruits[1]="pomegranate"
print("after changing the value of 1st index")
print(fruits)
fruits.append("badam")
#the value is added to the last index 
print("after using append the value will be added ")
print(fruits)

#inserting 
print("extending a list by adding multiple values")
fruits.extend(["nouman","aakif"])
print(fruits)
