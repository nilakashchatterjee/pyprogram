# 3. Write a function in Python to accept one decimal number and convert into equivalent binary number.
def decimalToBinary(num): #function converts decimal number to binary 
    if num > 1:
        decimalToBinary(num // 2)
    print(num % 2, end='')


# decimal number
number = int(input("Enter any decimal number: "))

# calling function
print("The binary number is: ",end="")
decimalToBinary(number)