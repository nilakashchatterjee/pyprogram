# Assignment 6
# Python program to calculate length of a string using recursion 
str = input("Enter a string:")
  
def strlen(str) : 
    if str == '': 
        return 0
    else : 
        return 1 + strlen(str[1:])  
      
print (strlen(str)) 
  
