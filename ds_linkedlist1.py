class Node:
    def __init__(self,item):
        self.item = item
        self.next = None
            
class llk:
    def __init__(self,item):
        n=Node(item)
        self.start=n
        self.last= self.start
    def insertfirst(self,item):
        n= Node(item)
        n.next= self.start
        self.start=n
    def display(self):
        n=self.start
        while n!= None:
            print(n.item,end="->")
            n=n.next
        print("Null")
               

l= llk(10)
l.insertfirst(15)
l.insertfirst(10)
l.display()
        

    








# class Node:

# 	def __init__(self, data):
# 		## data of the node
# 		self.data = data

# 		## next pointer
# 		self.next = None

# class LinkedList:

# 	def __init__(self):
# 		## initializing the start with None
# 		self.start = None

# 	def insert(self, new_node):
# 		## check whether the start is empty or not
# 		if self.start:
# 			## getting the last node
# 			last_node = self.start
# 			while last_node.next != None:
# 				last_node = last_node.next

# 			## assigning the new node to the next pointer of last node
# 			last_node.next = new_node

# 		else:
# 			## start is empty
# 			## assigning the node to start
# 			self.start = new_node

# 	def display(self):
# 		## variable for iteration
# 		temp_node = self.start

# 		## iterating until we reach the end of the linked list
# 		while temp_node != None:
# 			## printing the node data
# 			print(temp_node.data, end='->')

# 			## moving to the next node
# 			temp_node = temp_node.next

# 		print('Null')


# if __name__ == '__main__':
# 	## instantiating the linked list
# 	linked_list = LinkedList()

# 	## inserting the data into the linked list
# 	linked_list.insert(Node(1))
# 	linked_list.insert(Node(2))
# 	linked_list.insert(Node(3))
# 	linked_list.insert(Node(4))
# 	linked_list.insert(Node(5))
# 	linked_list.insert(Node(6))
# 	linked_list.insert(Node(7))

# 	## printing the linked list
# 	linked_list.display()