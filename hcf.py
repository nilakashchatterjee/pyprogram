# Python program to find H.C.F of two numbers
# define a function
def hcf(x, y):
    # checking for smaller number
    if x > y:
        small = y
    else:
        small = x
    for i in range(1, small+1):
        if((x % i == 0) and (y % i == 0)):
            hcf = i 
    return hcf

a = int(input("Enter the first number:"))
b = int(input("Enter the second number:"))

print("The H.C.F. is", hcf(a,b))