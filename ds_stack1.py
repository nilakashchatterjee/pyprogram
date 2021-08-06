# Basic operations on the Stack (push,pop,peek)
class Stack:
    def __init__(self):
        self.stack = []
    
    # Use list append method to push element
    def push(self, data):
        if data not in self.stack:
            self.stack.append(data)
            return True
        else:
            return False
    
    # Use list pop method to delete the top element
    def pop(self):
        if len(self.stack) <= 0:
            return ("No Element in the stack")
        else:
            return self.stack.pop()

    # Use peek to look at the top of the stack
    def peek(self):
        return self.stack[-1]

    def display(self):
        return (self.stack)

stk = Stack()
stk.push("Audi")
stk.push("Lamborghini")
print("First Peek:",stk.peek())
stk.push("BMW")
stk.push("Rolls Royce")
print("Second Peek:",stk.peek())
stk.push("Alpha Romeo")
stk.push("Mustang")
print("Displaying Stack Before pop Operation:",stk.display())
print("\nStarting pop operation:")
print(stk.pop())
print(stk.pop())
print("Displaying Stack After pop Operation",stk.display())