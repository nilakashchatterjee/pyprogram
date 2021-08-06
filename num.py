from numpy import *

arr = array([1,2,3],float) #we can change the type or it has the ability for implicit conversion
print(arr)

k= linspace(0,15,16) #Return evenly spaced numbers over a specified interval.
print(k)

s=logspace(1,20,10)
print(s)

p= arange(1,15,1)
print(p)

z= zeros(5,int) #we can the data type
print(z)

o= ones(5) #we can the data type
print(o)

m = random.rand(5) #generates random numbers between 0 to 1
print(m)

m = random.randint(10,size=(5)) #generates random numbers between 0 to 10
print(m)

ar = array([1,2,3,4])

print("The array:",ar,"\nThe shape",shape(ar),"\nThe dimensions:",ndim(ar)) #printing array, then the shape and ndim returns the dimensions of the arrray
ar1=ar.reshape(2,2)
print("The array:",ar1,"\nThe shape",shape(ar1),"\nThe dimensions:",ndim(ar1))

m = random.randint(100,size=(12))
print("existing array:",m)
m1 = m.reshape(3,4) #converting 1d array to 2d array
print("After reshaping:\n",m1)
print("The shape:",shape(m1))
print("The dimension:",ndim(m1))
m1 = m.reshape(2,3,2) #converting 1d array to 3d array
print("After reshaping:\n",m1)
print("The shape:",shape(m1))
print("The dimension:",ndim(m1))

a= array([2,4,6,8,10])
b= array([1,2,3,4,5])
# all array operations
c= add(a,b)
print("The c:",c)
c= subtract(a,b)
print("The c:",c)
c= multiply(a,b)
print("The c:",c)
c= divide(a,b)
print("The c:",c)

#the matrix multiplication
a= array([2,4,6,8,10,12])
a1=a.reshape(2,3)
b= array([1,2,3,4,5,6])
b1=b.reshape(3,2)
c1=dot(a1,b1)
print("\nThe matrix multiplication:\n",c1)