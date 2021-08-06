# Determining Harshad Number and using Value error exception
try:
    num = int(input("Enter a number:"))
    copy = num
    sum = 0
except ValueError:
    print("VALUE ERROR \nThe given input is not an number")
else:
    while num != 0:
        r = num % 10
        sum = sum + r
        num = num//10
    if (copy % sum) == 0:
        print(f"{copy} is an harshad number")
    else:
        print("It is not an harshad number")        

