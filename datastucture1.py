# data structure using python
# array data structure
from array import *
arr = array('i',[1,2,3,4,5,6,7,8])
i = 0
for i in range(0,len(arr)):
    arr.pop(0)

print(arr)