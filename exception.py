def funct1(obj,index):
    print("value at position {} is {}".format(index,obj[index]))
l=[10,20,25,30,23]
try:
    funct1(l,2)
except IndexError:
    print("Got exception")
print("End of the program\n")

# raising exception
try:
    print("raise exception")
    raise IndexError #have to use buit-in exceptions
except IndexError:
    print("caught exception\n")

# user defined exception
class abc(Exception):
    pass
try:
    print("raise exception")
    raise abc # created abc exception
except abc:
    print("caught exception\n")

# try block exception may occur
# except for handling exception
# finally is must excute program block

def fetch(obj,index):
    print(obj[index])
l=[3,4,5,6]
try:
    fetch(l,6)
except:
    print("caught exception")
finally:
    print("have to print\n")
'''
try:
    a=10
    b=20
    lst=[10,12,14,34,45]
    print(ls[5])
except NameError:
    print("Name error happened")
except IndexError:
    print("Out of index")
except (NameError,IndexError):
    print("multiplt")
else:
    print("no error occur")
finally:
    print("must call")
'''

# exercise 1
food = ["chocolate", "chicken", "corn", "sandwich", "soup", "potatoes", "beef", "lox", "lemonade"]
fifth = []

for x in food:
    try:
        fifth.append(x[4])
    except IndexError:
        pass
   
print(fifth)

# exercise 2
def get_value(data_list, index):
    return data_list[index]

# Sample list data
my_list = ['a', 'b', 'c']

try:
    print(my_list[3])
except IndexError:
    print("Index error")
except ValueError: