def binary_search(array,lower,higher,y):
    if higher>=lower:
        mid=(higher+lower)//2
        if array[mid]==y:
            return mid
        elif array[mid] > y:
            return binart_search(array,lower,mid-1,y)
        else:
            return binary_search(array,higher,mid+1,y)
    else:
        return -1
array=[10,20,30,50,60]
y=30
result=binary_search(array,0,len(array)-1,y)
if result!=-1:
    print("element is present at index position",str(result))
else:
    print("element is not present in the array")
