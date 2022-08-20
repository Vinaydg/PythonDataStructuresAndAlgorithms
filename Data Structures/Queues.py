class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def enqueue(self, val):
        newNode = Node(val)
        if self.length == 0:
            self.first = newNode
            self.last = newNode
            self.length += 1
            return self.length
        self.last.next = newNode
        self.last = newNode
        self.length += 1
        return self.length

    def dequeue(self):
        if self.length == 0:
            return None
        removedNode = self.first
        if self.length == 1:
            self.first = None
            self.last = None
            self.length -= 1
            return removedNode.val
        self.first = removedNode.next
        self.length -= 1
        return removedNode.val


q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(40)
q.enqueue(50)
q.enqueue(60)
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
