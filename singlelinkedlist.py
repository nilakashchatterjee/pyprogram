class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    
    def __init__(self): #the constructor
        # its the creation of the linked list, so at first the list will be empty
        self.start= None
    
    #____________________INSERTION FUNCTIONS_________________________
    
    def insert_at_beg(self,data): #insertion in the beginning
        new = Node(data)
        new.next = self.start
        self.start= new
    
    def insert_at_end(self,data): #insertion in the end
        new = Node(data)
        # first it will check whether the list empty or not
        if self.start == None:
            self.start=new 
            return
        n=self.start
        while n.next != None:
            n=n.next
        n.next=new
    
    def insert_before_data(self,data,x): #insertion before the specific data
        if self.start == None:
            print("List is Empty!!!")
            return
        
        if x == self.start.data:
            new=Node(data)
            new.next = self.start
            self.start = new
            return
        n=self.start
        while n.next != None:
            if n.next.data == x:
                break
            n=n.next
        if n.next == None:
            print("The Item is not in the list")
        else:
            new=Node(data)
            new.next=n.next
            n.next=new

    def insert_after_data(self,data,x): #insertion after the specific data
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

    def insertion_at_index(self,data,index): # insertion of data at a specified index
        if index == 1:
           new = Node(data) 
           new.next = self.start
           self.start = new
        i=1
        n=self.start
        while i< index-1 and n != None:
            n=n.next
            i+=1
        if n == None:
            print("Index out of bound")
        else:
            new = Node(data)
            new.next = n.next
            n.next = new

    #____________________DELETION FUNCTIONS_________________________

    def delete_at_beg(self): # deletion of the element from the beginning
        if self.start == None:
            print("No element in the list")
            return
        # print("After deletion from begining:")
        self.start = self.start.next

    def delete_at_end(self): # deletion of the element from the end
        if self.start == None:
            print("No element in the list")
            return
        n=self.start
        while n.next.next != None:
            n=n.next
        n.next=None
    
    def delete_by_data(self,x): # deleting data by value
        if self.start == None:
            print("No element in the list")
            return
        if self.start.data == x:
            self.start = self.start.next
            return
        n=self.start
        while n.next != None:
            if n.next.data == x:
                break
            n=n.next
        if n.next == None:
            print("Item is not found in the list")
        else:
            n.next = n.next.next


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
lnk.insert_after_data(60,40)
lnk.insert_before_data(50,40)
lnk.insertion_at_index(70,2)
lnk.insertion_at_index(45,3)
lnk.traverse()

# lnk.delete_at_beg()
# lnk.delete_at_end()
lnk.delete_by_data(60)
lnk.traverse()