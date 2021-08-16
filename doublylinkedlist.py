class Node:
    def __init__(self,data):
        self.data= data
        self.next=None
        self.prev=None

class DoublyLinkedlist:
    def __init__(self):
        self.start = None

    def insert_at_beg(self,data):
        if self.start == None:
            new = Node(data) 
            self.start = new
            return
        new = Node(data)
        new.next= self.start
        # self.start.prev = new
        self.start = new
    
    def insert_at_end(self,data):
        if self.start == None:
            new = Node(data)
            self.start = new
            return
        n = self.start
        while n.next != None:
            n = n.next
        new = Node(data)
        n.next = new
        new.prev = n

    def insert_before_data(self,data,x):
        if self.start == None:
            print("The list is Empty!!!")
            return
        else:
            n = self.start
            while n != None:
                if n.data == x:
                    break
                n = n.next
            if n == None:
                print("Data is not found in he list!!!")
            else:
                new = Node(data)
                new.next = n
                new.prev = n.prev
                if n.prev != None:
                    n.prev.next = new
                n.prev = new
    
    def insert_after_item(self,data,x):
        if self.start == None:
            print("The list is empty!!!")
            return
        else:
            n= self.start
            while n != None:
                if n.data == x:
                    break
                n = n.next
            if n == None:
                print("Data is not found in the list!!!!")
            else:
                new = Node(data)
                new.prev = n
                new.next = n.next
                if n.next != None:
                    n.next.prev= new
                n.next = new

    def traverse_list(self):
        if self.start == None:
            print("List has no element")
            return
        else:
            n = self.start
            while n is not None:
                print(n.data ,end="->")
                n = n.next
            print("NULL")

dlk = DoublyLinkedlist()
dlk.insert_at_beg(15)
dlk.insert_at_beg(14)
dlk.insert_at_beg(13)
dlk.insert_at_beg(12)

dlk.insert_at_end(16)
dlk.insert_at_end(17)
dlk.insert_at_end(18)

dlk.insert_before_data(188,18)
dlk.insert_after_item(121,188)
dlk.traverse_list()