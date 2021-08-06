#adding values to the elements of the array
arr = array([1,2,3,4,5])
arr = arr + 5
print(arr)

#adding two arrays
arr1 = array([1,2,3,4,5])
arr2 = array([6,7,8,9,10])
arr3 = arr1 + arr2 
print(arr3) #its a vectorized operation

arr4 = array([8,14,2,23,0])

#passing basic mathematical fuction to the array
arr = array([1,2,3,4,5])
print(sin(arr)) #we can use cos tan etc

print(log(arr)) #logarithmic value of each element

print(square(arr)) #or we can use print((arr)**2)  #square value of each element

print(sqrt(arr)) #squareroot value of ecah element

print(sum(arr)) #sum of elements of array

print(min(arr)) #minimum value element in the array

print(max(arr)) #max value element in the array

print(concatenate([arr1,arr2])) #concatenate two arrays

print(sort(arr4)) #sort array