def compound_interest(p,r,t):
    c=p*pow((1+(r/100)),t)
    return c
p=int(input("enter the principle amount:"))
r=int(input("enter the rate:"))
t=int(input("enter the time:"))
c=compound_interest(p,r,t)
print("compound interest is",format(c,'.2f'))

