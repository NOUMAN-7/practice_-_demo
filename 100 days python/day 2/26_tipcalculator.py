print("Welcome to the tip calculator!")
bill=float(input("what is the total bill?"))
tip=int(input("How much tip would you like to give? 10,12,or,15?"))
split=int(input("How many people to split the bill?"))
#the tip is in percentage so we should divide it by 100 
tip_as_percentage=tip/100
total_tip_amount=bill*tip_as_percentage
total_bill=bill+total_tip_amount
bill_per_person=total_bill/split
final_amount=round(bill_per_person,2)
print(f"Each person should pay:{final_amount}")


