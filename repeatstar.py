#ass 6 q1
def fun(str1):
    new_str = ""
    for i in str1:
        if i in new_str:
            new_str += "*"
        else:
            new_str += i
    return new_str

print(fun("Hello World"))
