# Assignment 6
# pass value to a formula y=6x^2+3x+2 
def formula(x):
    y = (6*(x**2))+(3*x)+2
    return y
a = int(input("Enter a value of x:"))
print(formula(a))