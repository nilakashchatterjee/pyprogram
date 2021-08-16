# Name : Nilakash Chatterjee
# 2nd semester Data Structure with Python (Practical Exam)
# Date: 16/08/2021
#ROLL NO:33671020035



# Q1. Create a singly linked list of natural numbers (1<=node.item<=9) and return TRUE if the list IS Palindrome else return FALSE.
# Input: head = [1,2,2,1] 
# Output: true   
 
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
 
 
def isPalindrome(start):
 
    # constructing an empty stack
    s = []
 
    # push all elements of the linked list into the stack
    n = start
    while n:
        s.append(n.data)
        n = n.next
    
    print("\nThe linked list is", end="--> ")
    for i in range(len(s)):
        print(s[i],end=" ")
    n = start
    while n:
 
        top = s.pop()
 
        # comparing the popped element with the current node's data return false if mismatch happens
        if top != n.data:
            return False
 
        n = n.next
    #returns true if the the popped element matches with the current node's data
    return True
 
 
if __name__ == '__main__':
 
    start = Node(1)
    start.next = Node(2)
    start.next.next = Node(3)
    start.next.next.next = Node(2)
    start.next.next.next.next = Node(1)
 
    print("\n",isPalindrome(start))