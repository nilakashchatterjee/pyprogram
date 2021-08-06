# def funct1(obj,index):
#     print("value at position {} is {}".format(index,obj[index]))
# l=[10,20,25,30,23]
# try:
#     funct1(l,2)
# except IndexError:
#     print("Got exception")
# print("End of the program")

# # raising exception
# try:
#     print("raise exception")
#     raise abc
# except IndexError:g
#     print("caught exception")
# lst=[2,3,4,5,6,7,8]
# print(lst.index(8))
# import math as m
# print(math.sqrt(81))
# s=set('abc')
# s.add('mno')
# s.update(set(['p','q']))
# print(s)
# i=9
# j=7


# class  A:
#     def __init__(self):
#         self.mul(15)
        
#     def mul(self,i):
#         self.i=4*i

# class B(A):
#     def __init__(self):
#         super().__init__()
#         print(self.i)
#     def mul(self,i):
#         self.i=2*i
# obj=B()

        
# class error(Exception):
#     def __init__(self,num):
#         self.num=num
# try:
#     raise error(123)
# except error as e:
#     print("reciebed error",e.num)

# for i in range(5):
#     if i==3:
#         break
#     print(i)


def scope_test():
    def do_local():
        spam="local spam"
    def do_nonlocal():
        nonlocal spam
        spam= "nonlocal spam"
    def do_global():
        global spam
        spam="global spam"