#here we will take user input from user
a=float(input("Enter 1st Number: "))
b=float(input("Enter 2nd Number: "))
c=a+b
print(f"The sum of {a} and {b} is {c}") #using f-string formatting

'''
a = 10
b = 20
c = a + b

#Normal string concatenation
print("sum of", a , "and" , b , "is" , c) 

#convert variable into str
print("sum of " + str(a) + " and " + str(b) + " is " + str(c)) 

# if you want to print in tuple way
print("Sum of %s and %s is %s: " %(a,b,c))  

#New style string formatting
print("sum of {} and {} is {}".format(a,b,c)) c

#in case you want to use repr()
print("sum of " + repr(a) + " and " + repr(b) + " is " + repr(c))

EDIT :

#New f-string formatting from Python 3.6:
print(f'Sum of {a} and {b} is {c}')
'''