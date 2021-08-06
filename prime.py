# In this program we will print prime numbers between 100 and 30
num=100
count=0
print("Prime numbers from 100 to 30 are:",end=" ")

while num>=30:
   # all prime numbers are greater than 1
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num,end=" ")
            count+=1
    num-=1
print("\nTotal prime numbers are:",count)