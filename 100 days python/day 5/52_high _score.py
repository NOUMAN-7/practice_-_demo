#getting input in list
student_scores=input("enter the score:").split()
for i in range(0,len(student_scores)):
    student_scores[i]=int(student_scores[i])
#the value will be 0 at before the loop after getting inside the loop the highest value will be change if score is greater then the highest score
#then highest value  will the score which you have entered 
hightest_score=0
for score in student_scores:
    #if 
    if(score>hightest_score):
        hightest_score=score
print(hightest_score)
