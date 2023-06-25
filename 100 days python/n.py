name1=input()
name2=input()
n1count=0
n2count=0
for i in name1:
    n1count=n1count+1
for i in name2:
    n2count=n2count+1
    
count = 0
countq = 0
if(n1count==n2count):
    for i in range(n1count):
        if name1[i] != '?' and name2[i] != '?' and name1[i] != name2[i]:
            count+=1
        if name1[i] == '?' or name2[i] == '?':
            countq+=1
countq=count+countq
print(count,countq)