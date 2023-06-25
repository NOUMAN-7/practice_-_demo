str1=input()
str2=input()
count1=0
count2=0
res1=0
res2=0
for i in str1:
    res1=res1+1
for i in str2:
    res2=res2+1
if res1==res2:
    for i in range(res1):
        if (str1[i]!='?' and str2[i]!='?' and str1[i]!=str2[i]):
            count1=count1+1
        if str1[i]=='?' or str2[i]=='?':
            count2=count2+1

count2=count1+count2
print(count1,count2)