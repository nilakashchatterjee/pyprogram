# Name : Nilakash Chatterjee
# 1st semester Python Practical Exam
# Date: 15/06/2021
#ROLL NO:33671020035

#1) WAP in python to handle "list assignment index out of range" exception along with a "finally" block
def funct1(obj,index):
    print("value at position {} is {}".format(index,obj[index]))

l=[10,20,25,30,23]
try:
    funct1(l,5)
except IndexError:
    print("Got exception -> IndexError")

finally:
    print("The statement in the final block!!!")
