import random
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
'''''
#using with out  choice method
size=len(names)
random_choice=random.randint(0,size-1)
person=names[random_choice]
print(f"{person} is going to buy the meal today!")
'''''
#with choice method
person=random.choice(names)
print(f"{person} is going to buy the meal today!")


                                                                                                                                                                                                                                                                                                                                                               