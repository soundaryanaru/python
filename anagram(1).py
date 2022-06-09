a="abcd"
b=str(input("enter the string:"))
c={}
d={}
for i in a:
    m=a.count(i)
    if i not in c:
        c[i]=m
for j in b:
    n=b.count(j)
    if j not in d:
        d[j]=n
print(c)
print(d)
if c.items()==d.items():
    print("it is anagram")
else:
    print("not anagram")
        
