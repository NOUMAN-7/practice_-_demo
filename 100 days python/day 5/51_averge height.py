student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])


#total height  which we can get  by adding all  student height  in a class

total_height=0
for height in student_heights:
    total_height+=height
#print(f"total height of a student  in class :{total_height}")

#total length of the list
number_of_student=0
for student in student_heights:
    number_of_student+=1
#print(f"total number of student in class :{number_of_student}")


average_height=round(total_height/number_of_student)

print(average_height)
