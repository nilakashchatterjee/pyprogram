class Queue:
    def __init__(self):
        self.queue = []
    
    def push(self,dataval):
    # Insert method to add element
        if dataval not in self.queue:
            self.queue.insert(0,dataval)
            return True
        return False
    def size(self):
        return len(self.queue)
    def show(self):
        return self.queue

TheQueue = Queue()
TheQueue.push("Mon")
print(TheQueue.show())
TheQueue.push("Tue")
print(TheQueue.show())
TheQueue.push("Wed")
print(TheQueue.show())
print(TheQueue.size())