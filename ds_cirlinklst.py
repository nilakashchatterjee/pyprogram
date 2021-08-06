class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linklist:
    def __init__(self,data):
        # self.start=node(data)
        n= node(data)
        self.start=n
        n.next=self.start
    def insertlast(self,data):
        n=node(data)
        a=self.start
        while(a.next!=self.start):
            a=a.next
        a.next=n
        n.next=self.start