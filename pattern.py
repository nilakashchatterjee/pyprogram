n=int(input("Enter the number of columns:"))

for i in range(n):
    for j in range(n):
        print("* ",end="")
    print()

print()
k=1
for i in range(1,n+1):
    for j in range(i+1):
        print(k,end="\n")
        k+=1
    print(end=" ")
print()

for i in range(n):
    for j in range(n-i):
        print("* ",end="")
    print()
print() 

# def tripat():
#     ran= int(input("Enter number:"))
#     for i in range(1,ran+1):
#         print("*" *i)
#     print("\n")
    
#     k=1
#     j=1
#     for i in range(1,ran+1):
#         print(" "*(ran-k) + "O"*(j))
#         k+=1
#         j+=2
#     print("\n")

#     m=ran
#     p=(ran*2)-1
#     while m!=0:
#         print(" "*(ran-m) + "O"*p)
#         m-=1
#         p-=2
#     print("\n")



# if __name__=="__main__":
#     tripat()