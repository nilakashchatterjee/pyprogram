def name(lst):
    
    more=0
    less=0

    for i in range(len(lst)):
        if len(lst[i])>5:
            more+=1
        else:
            less+=1
    return more,less

lst=[]
x=int(input("How many names do you want to enter: "))

for k in range(x):
    lst.append((input()))

more,less= name(lst)
print("Names more than 5 character: {} and Names less than 5 character: {} ".format(more,less))