# Program to determine whether the number is even or odd and using user-defined exceptions
class Error(Exception):
    """Base class for other exceptions"""
pass

class UnsignedIntegerError(Error):
    """Raised when the input value has signed integer"""
    pass

try:
    num = int(input("Enter a number:"))
    if num < 0:
        raise UnsignedIntegerError
except UnsignedIntegerError:
    print("UNSIGNED INTEGER ERROR \nThe number is negetive!!!")
    
else:
    if (num%2)==0:
        print("The given input is even number")
    else:
        print("The given input is odd number")