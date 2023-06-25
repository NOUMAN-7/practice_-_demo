sum=0
for numbers in range(2,101,2):
    sum+=numbers
print(sum)

print("another method to print even numbers")
#another method to print even number
sum=0
for numbers in range(1,101):
    if numbers%2==0:
        sum+=numbers
print(sum)

