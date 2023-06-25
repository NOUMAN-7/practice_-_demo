
def findLen(str):
	counter = 0
	for i in str:
		counter += 1
	return counter

if __name__=='__main__':
	n1 =input()
	n2 =input()
	l1=(findLen(n1))
	l2=(findLen(n2))
	count=0
	cq=0
	if l1(n1)==l2(n2):
		print("ok")
