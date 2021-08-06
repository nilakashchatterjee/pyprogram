# Printing a patten of 0 and 1
# 0
# 1 0
# 0 1 0
# 1 0 1 0
n = int(input("Enter the number of columns:"))
for i in range(0,n):
    for j in range(0,i+1):
        if (i+j)%2==0:
            print("0",end=" ")
        else:
            print("1",end=" ")
    print()
