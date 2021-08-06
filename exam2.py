# 2. WAP in Python to create a dictionary from user input.

n = int(input("Number of data to be entered: "))
dictionary = {}

for i in range(n):
	key = input("Enter key for dictionary:")
	value = input("Enter value for dictionary:")
	dictionary[key] = value
    
print("The dictionary from the user input is:\n",dictionary)