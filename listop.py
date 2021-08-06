# this program demonstrates the function of list

grocery = ["sunlight","vim bar", "deodrant","potato","candy",56] #its a mixed list
print(grocery)
print(grocery[3])
numbers = [45, 17, 9, 22, 15] #list index starts from 0
print(numbers)
print(numbers[4])
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)
print(numbers[1:4])
print(numbers[::2])
print(numbers[::-1]) #reverses the string
print(len(numbers))
print(max(numbers))
print(min(numbers))
numbers.append(50)
print(numbers)
numbers.insert(1,8)
print(numbers)
numbers.remove(9) #removes desired value
print(numbers)
numbers.pop() #removes end value
print(numbers)
numbers[3] = 100  #lits are mutable
print(numbers)

#now dealing with tuple

tp = (1,5,3,88,4) #tuples are immutable
print(tp)