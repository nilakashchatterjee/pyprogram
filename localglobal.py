x = "Nilakash" #global variable
def myfunc():
    x = "Chatterjee" #treating x as local variable
    print(x) 

myfunc() #this function will the local variable value

print(x) #this will print the the global variable

#now implementing global variable in local scope

y = "Volleyball" #initial global variable 
def anofunc():
    global y #modifying y in local scope by using the global keyword
    y= "awesome"
    print(y) #prints the local y 

anofunc()
print(y) #prints the modified y in local scope

