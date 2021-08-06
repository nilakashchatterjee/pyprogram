'''
def update(lst):
    print(id(lst))
    lst[1]=25
    print("after",id(lst))
    print("x", lst)

lst=[10,20,30]
print(id(lst))
update(lst)
print("a",lst)
'''

def person(name,age):
    print(name)
    print(age)
person("Nilakash",20)
person(age=20,name="Nilakash")

def sum(*b):  #it creates b as tuple
    c=0 
    for i in b: #adding each value to c
        c=c+i
    print(c)

sum(4,5,5,3)


def person1(name, **data):
    print(name)
    for i,j in data.items():
        print(i,j)  #we can also use print(data)
person1("Nilakash",age=20,city="Siliguri",mob=8436610217)

