# Python Program to show the number of iteration in both binary and linear search algorithms
def linearsearch(arr, x):
   count = 0  # counter for linear search iteration
   for i in range(len(arr)):
      count +=1
      if arr[i] == x:
         return i,count
   return -1

def binarysearch(arr,val):
    low =0
    high = len(arr) -1
    mid = 0
    count = 0  # counter for binary search iteration
    while low <= high:
        count += 1
        mid = (high + low) // 2

        if arr[mid] < val:
            low = mid + 1
        elif arr[mid] > val:
            high = mid - 1
        else:
            return mid,count
    return -1

arr = list(range(1,101)) # array from 1 to 100
n = int(input("Enter the page number to be searched:"))

resultbin , countbin = binarysearch(arr,n)
print("From Binary Search:")
if resultbin != -1:
    print("The element is present at index(using binary search)",resultbin+1)
    print("Number of iterations it have:",countbin)
else:
    print("The element is not found in the list")

result , count = linearsearch(arr,n)
print("\n\nFrom Linear Search:")
if result != -1:
    print("The element is present at index",result+1)
    print("Number of iterations it have:",count)
else:
    print("The element is not found in the list")

