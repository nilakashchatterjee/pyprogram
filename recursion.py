# Get a list of integers from user and calculate the total sum of the elements using recursion
def addition(lst,n):
    if n <= 0:
        return 0
    else:
        return lst[n-1] + additon(lst,n-1)
n = int(input("Enter the range of the list:"))
lst1 = [] 
print("Enter the values:")
for i in range(0, n): 
    ele = int(input()) 
    lst1.append(ele)
p=addition(lst1,len(lst1))
print("The sum of the elements in list is:",p)