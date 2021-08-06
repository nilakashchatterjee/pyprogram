# 5. Print the pattern.

# 0 1 0 1 0
# 1 0 1 0
# 0 1 0
# 1 0
# 0

n = int(input("Enter the number of columns:"))
for i in range(n + 1, 0, -1):    
    for j in range(0, i - 1):  
        if (i+j)%2==0:
            print("0", end=' ') 
        else:
            print("1",end=" ") 
    print(" ")  