n = int(input("Enter the range of the first list:"))
c=0
lst1 = [] 
print("Enter the values:")
for i in range(0, n): 
    ele = int(input()) 
  
    lst1.append(ele) # adding the element to the end of the list
for i in lst1:
    if i%2 == 0:
        c+=1
    
print("Total numbers of even numbers are:",c)
