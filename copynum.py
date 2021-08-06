from numpy import *

#aliasing
a=array([1,2,3,4,5])
b=a
a[1]=0
print(a)
print(b) 
'''
arrays a and b have same address in memory,this method of copying is known alaising
changes in array a will also reflected be in array b
'''
print(id(a))
print(id(b))

#shallow copy
a=array([1,2,3,4,5])
b=a.view()
a[1]=0
print(a)
print(b) 
'''
arrays a and b have different address in memory,this method of copying is known shallow copying
changes in array a will also reflected be in array b
'''
print(id(a))
print(id(b))

#deep copy
a=array([4,8,7,2])
b=a.copy()
a[1]=0
print(a)
print(b)
'''
arrays a and b have different address in memory,this method of copying is known as deep copy
changes in array a will not reflected in array b
'''
print(id(a))
print(id(b))
