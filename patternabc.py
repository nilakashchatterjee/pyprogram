# In this program we are printing the pattern 
# a
# b c
# d e f
# g h i j
n = int(input("Enter the number of columns:"))
k=97
for i in range(0,n):
    for j in range(0,i+1):
        print(chr(k),end=" ")
        k+=1
    print()
