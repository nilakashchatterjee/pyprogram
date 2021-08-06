# In this program we are taking 5 consecutive prime numbers are printing their average
ar = []
num=2
count=0
s=0
while len(ar)<5:
    for i in range(2,num):
        if num % i ==0:
            break
    else:
        ar.append(num)
        count+=1
    num+=1
print("List after inserting the prime numbers\n",ar)
for i in range(len(ar)):
    s=s+ar[i]
avg= s/count
print("Sum is:",s)
print("Average is:",avg)