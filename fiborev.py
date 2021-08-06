# Python program to print Fibonacci Series upto 100 in reverse order
n1,n2 = 0,1
l = []
print("Fibonacci Sequence:",end="")
while n1 < 100:
    l.append(n1)
    n = n1 + n2
    n1 = n2
    n2 = n
print(l[::-1]) #printing the list in reverse order

