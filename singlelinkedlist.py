class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    
    def __init__(self):
        # its the creation of the linked list, so at first the list will be empty
        self.start= None
    
    def insert_at_beg(self,data):
        new = Node(data)
        new.next = self.start
        self.start= new
    
    def insert_at_end(self,data):
        new = Node(data)
        # first it will check whether the list empty or not
        if self.start == None:
            self.start=new 
            return
        n=self.start
        while n.next != None:
            n=n.next
        n.next=new
    
    def insert_after_data(self,data,x):
        if self.start==None:
            print("List is empty!!!")
            return
        n=self.start
        while n != None:
            if n.data==x:
                break
            n=n.next
        if n == None:
            print("Item not present in the list")
        else:
            new=Node(data)
            new.next=n.next
            n.next=new

    def traverse(self):
        if self.start == None:
            print("The list is empty")
        else:
            n=self.start
            while n != None:
                print(n.data,end="->")
                n=n.next
            print("NULL") 


lnk=LinkedList()
lnk.insert_at_beg(15)
lnk.insert_at_beg(5)
lnk.insert_at_end(20)
lnk.insert_at_end(40)
lnk.insert_after_data(60,20)
lnk.traverse()