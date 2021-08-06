a=20
def intlistfrominput(str1):
    y = str1.split(",")
    num = [int (i) for i in y]
    return num

def sum(lst):
    sum = 0
    for i in lst:
        sum = sum + i
    return sum