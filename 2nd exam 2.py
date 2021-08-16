# Name : Nilakash Chatterjee
# 2nd semester Data Structure with Python (Practical Exam)
# Date: 16/08/2021
#ROLL NO:33671020035

# Q2. Create a singly linked list of natural numbers.
# If there are two middle nodes then return the list that appears on left side of the middle nodes in the linked list otherwise return list that appears right hand side of the middle node.


# Example 1
# Input : [1,2,3,4,5,6,7]
# Output: [5,6,7]


# Example 2
# Input : [1,2,3,9,9,5,6,7]
# Output: [1,2,3]


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
 
 
def linkedlist(start):
 
    # constructing an empty stack
    s = []
 
    # push all elements of the linked list into the stack
    n = start
    # c=0
    while n:
        s.append(n.data)
        n = n.next
    
    l = len(s)
    print("\nThe linked list is", end="--> ")
    for i in range(l):
        print(s[i],end=" ")
    
    
    if l%2 != 0:
        print("\n\nWhen the list have odd number of items -> ",end=" ")
        for i in range ((l//2)+1,l):
            print (s[i],end=" ")
    else:
        print("\n\nWhen the list have even number of items -> ",end=" ")
        for i in range((l//2)-1):
            print (s[i],end=" ")
    
if __name__ == '__main__':
 
    start = Node(1)
    start.next = Node(2)
    start.next.next = Node(3)
    start.next.next.next = Node(9)
    start.next.next.next.next = Node(9)
    start.next.next.next.next.next = Node(5)
    start.next.next.next.next.next.next = Node(6)
    # start.next.next.next.next.next.next.next = Node(7)

    linkedlist(start)