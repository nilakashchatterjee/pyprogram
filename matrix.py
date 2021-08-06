from numpy import *

a = array ([
                [1,2,3,4],
                [5,6,7,8]
            ])

m1 = matrix(a)
print(m1,"\n")

n = matrix("2 1 4 ; 6 8 9 ; 10 11 12")   # we can create matrix without creating array previously
m = matrix("7 3 8 ; 5 2 4 ; 11 13 15")
print(n,"\n")

print(diagonal(n))
print(diagonal(fliplr(n)),"\n")

print(n.min())
print(n.max(),"\n")

ad = n+m
print(ad,"\n") #addition
mul = n*m
print(mul,"\n") #multiplication
sub = n-m
print(sub,"\n") #subtraction


