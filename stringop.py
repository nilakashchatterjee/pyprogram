#indices in python starts from 0
mystr="i am nilakash"

print(len(mystr)) # returns the length of the string from 0 to 12

print(mystr[5]) #printing the 5th character ie "n"

# ':' -> this symbol is used for string slicing

print(mystr[0:5])  #prints character from 0th to 4th position ,excluding the 5th position 

print(mystr[0:19])  #prints character from 0th to 18th position, have to write one extra in the end 

print(mystr[0:19:2]) #print character with the gap of two characters

print(mystr[:19]) #print from the starting point if start value is blank

print(mystr[0:]) #print to the end point if end value is blank

print(mystr[::]) #prints entire string, as it consider default values ie [0:19:1]

print(mystr[::-1]) #prints the string in backwards

print(mystr.isalnum()) #The isalnum() method returns True if all the characters are alphanumeric, meaning alphabet letter (a-z) and numbers (0-9).Example of characters that are not alphanumeric: (space)!#%&? etc.

print(mystr.isalpha()) #The isalpha() method returns True if all the characters are alphabet letters (a-z). Example of characters that are not alphabet letters: (space)!#%&? etc.

print(mystr.endswith("akash")) #The endswith() method returns True if the string ends with the specified value, otherwise False.

print(mystr.count("a")) #count specific value

print(mystr.capitalize()) #Upper case the first letter in this sentence

print(mystr.upper()) #uppercase the entire string

print(mystr.lower()) #lowercase the entire string

print(mystr.find("am")) #returns strings position

print(mystr.replace("nilakash","neil")) #replaces string/character with a given string/character