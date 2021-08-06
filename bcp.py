'''This is a demonstration of break continue and pass statement'''

#break statement

av=10 #available candies
x=int(input("How many Candies you want? "))
i=1
while i<=x:
    
    if i>av:
            print("Out of Stock")
            break
    
    print(i,"Candy")
    i+=1
print("End")

#continue statement
#printing numbers 1 to 100 excluding the numbers divisibles 3 or 5
for i in range (101):
    if i % 3==0 or i % 5==0:
        print(end="")
        continue
    print(i,end=" ")

print("\nEnd")

#pass statement
#printing numbers 1 to 100 excluding the odd numbers 
for i in range(101):
    if(i%2!=0):
        pass
    else:
        print(i,end=" ")

print("\nFinally ends")

