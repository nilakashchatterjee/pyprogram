from array import *
'''
val = array('i',[5,4,6,7])

#copying array
nw= array(val.typecode,(a for a in val))
for i  in nw :
    print(i)
'''

arr = array('i',[])

n = int(input("Enter the length of the array:"))

print("Enter the values:")
for i in range(n):
    x = int(input())
    arr.append(x)
print(arr)

k=0
val = int(input("Enter a Value:"))
for e in arr:
    if e==val:
        print(k)
        break
    k+=1

print(arr.index(val))