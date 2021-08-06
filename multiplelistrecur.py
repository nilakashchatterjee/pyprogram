# Get two or more list from the user and find the sum of the elements of each list display that using recursion
def add(lst,n):
    if n <= 0:
        return 0
    else:
        return lst[n-1] + add(lst,n-1)

count = int(input("Enter the number of list you want:"))
print("Total numbers of list we are using:",count)
lst = [[] for i in range(0,count)]
a=[]
n = int(input("Enter the range of the list:")) 
for k in range(0,count):    
    print("Enter the values list:",k+1)
    for i in range(0, n): 
        ele = int(input()) 
        lst[k].append(ele)
    print(lst[k])
    a.append(add(lst[k],n))
    

for i in range(0,count):
    print(f"Sum of list is",i+1,":",a[i])