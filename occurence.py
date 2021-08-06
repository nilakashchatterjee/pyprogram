l1 = [3,2,5,3,2,7]
i=0
while i<len(l1):
    item=l1[i]
    if item in l1[i+1: ]:
        l1.pop(i)
        continue
    i=i+1
print(l1)

# while
# item = l1[0]
# if item in l1[1:]:
#     l1.remove(item)
# print(l1)

