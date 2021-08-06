# assingment 6 q5
#python program to get minimum 3 character input replace it by "ing" or if ing already exists then replace it by "ly"
def string(st):
    l = len(st)
    if l > 2:
        if st[-3:] == "ing":
            st += "ly"
        else:
            st += "ing"
    return st
a = input("Enter a string:")
print(string(a))
