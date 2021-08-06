#This is a program to print numbers from 1 to 100 
#And Skip the numbers which are divisible by 3 and 5

i=1
while i <= 100:
    if (i%3==0 or i%5==0 ):
        print(end="")
    else:
        print(i, end=" ")
    
    i=i+1    
    

        