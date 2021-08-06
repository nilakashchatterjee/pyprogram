
# l = [[1,2,3],90,89,66,[4,5,6],[7,8,9],12,11]
 
# output = []
  
# def string(l):
#     for i in l:
#         if type(i) == list:
#             string(i)
#         else:
#             output.append(i)
  

# print ('The original list: ', l)
# string(l)
# print ('The list after removing nesting: ', output)
# total = 0
# for ele in range(0, len(output)):
#     total = total + output[ele]
 

# print("Sum of all elements in given list: ", total)



def addElements(ll):
    sum = 0
    for i in ll:
        if type(i) == list:
            sum += addElements(i)
        else:
            sum += i
    return sum

# Taking user input:
l1 = []
n = int(input("How many elements to enter in list: "))
for i in range(n):
    ch = int(input(('''Choose what type of data to enter
        1. List 
        2. Single element
        Choice:''')))
    if ch in [1,2]:
        if ch == 1:
            x=[]  
            for i in range(int(input("How many elements are in list : "))):  
                x.append(int(input()))
            l1.append(x)
        elif ch == 2:
            el = int(input("Enter element to add:"))
            l1.append(el)
    else:
        print("Invalid choice")
        break
print("Sum of elements in the list:",addElements(l1))