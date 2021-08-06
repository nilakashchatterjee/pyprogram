n = int(input("Enter the number of columns:"))
for i in range(1,n+1):
    m = n-1
    for j in range(1,i+1):
        print(i,end=" ")
        i+=m
        m-=1
    print()