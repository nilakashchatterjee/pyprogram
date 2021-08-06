class node:
   def __init__(self,data):
       self.data =data
       self.prev=None
       self.next=None
class dlinklist:
    def __init__(self,data):
        n=node(data)
        self.start=n
    # def insertfirst(self,data):

    
    def  insertlast(self,data):
        n=node(data)
        n1=self.start
        while n1.next != None:
            n1=n1.next
        n1.next=n
        n.prev=n1
    def insertitem(self, x, data):
        if self.start == None:
            print("List is empty")
            return
        else:
            n = self.start
            while n != None:
                if n.data == x:
                    break
                n = n.next
            if n == None:
                print("item not in the list")
            else:
                new = node(data)
                new.prev = n
                new.next = n.next
                if n.next != None:
                    n.next.prev = new
                n.next = new
    def traverse(self):
        if self.start == None:
            print("No element in list")
            return
        else:
            n = self.start
            while n != None:
                print(n.data , " ")
                n = n.next


dl = dlinklist(10)
dl.insertlast(13) 
dl.insertlast(20)
dl.insertlast(30)
dl.insertlast(40)
dl.insertitem(50,14)

dl.traverse()
