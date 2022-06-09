n=int(input("enter length of the array:"))
l=[]
for i in range(0,n):
	a=int(input("enter elements:"))
	l.append(a)
l.sort()
lwr,mid=0,0
upr=len(l)-1
s=int(input("enter your number to search:"))
while (lwr<upr):
	mid=int ((lwr+upr)/2)
	if(s==l[mid]):
		print("element found in ",mid," position")
		break
	elif s< l[mid]:
		upr=mid-1
	else:
		lwr=mid+1
print(l)
