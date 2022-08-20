class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def push(self, val):
        newNode = Node(val)
        if self.length == 0:
            self.head = newNode
            self.tail = self.head
            self.length += 1
            return self
        self.tail.next = newNode
        newNode.prev = self.tail
        self.tail = newNode
        self.length += 1
        return self

    def pop(self):
        if self.length == 0:
            return "List is empty."
        popNode = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
            self.length -= 1
            return popNode
        self.tail = self.tail.prev
        self.tail.next = None
        popNode.prev = None
        self.length -= 1
        return popNode

    def shift(self):
        if self.length == 0:
            return "List is Empty"
        oldHead = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
            self.length -= 1
            return oldHead
        self.head = oldHead.next
        self.head.prev = None
        oldHead.next = None
        self.length -= 1
        return oldHead

    def traverse(self):
        current = self.head
        while current:
            print(current.val)
            current = current.next

    def unshift(self, val):
        newNode = Node(val)
        if self.length == 0:
            self.head = newNode
            self.tail = newNode
            self.length += 1
            return self
        self.head.prev = newNode
        newNode.next = self.head
        self.head = newNode
        self.length += 1
        return self

    def get(self, n):
        if n < 0 or n >= self.length:
            return "Invalid Index"
        if n <= self.length // 2:
            current = self.head
            count = 0
            while count != n:
                current = current.next
                count += 1
            return current
        if n > self.length // 2:
            current = self.tail
            count = 0
            while count < self.length - n - 1:
                current = current.prev
                count += 1
            return current

    def setval(self, index, val):
        current = self.get(index)
        if current != "Invalid Index":
            current.val = val
            return True
        return False

    def insert(self, index, val):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            self.unshift(val)
            return True
        if index == self.length:
            self.push(val)
            return True
        newNode = Node(val)
        nexNode = self.get(index)
        if nexNode != "Invalid Index":
            newNode.next = nexNode
            newNode.prev = nexNode.prev
            nexNode.prev.next = newNode
            nexNode.prev = newNode
            self.length += 1
            return True
        return False

    def remove(self, index):
        if index < 0 or index >= self.length:
            return "Invalid Index"
        if index == 0:
            self.length -= 1
            return self.shift()
        if index == self.length - 1:
            self.length -= 1
            return self.pop()
        current = self.get(index)
        prev = current.prev
        nex = current.next
        prev.next = nex
        nex.prev = prev
        current.next, current.prev = None, None
        return current

    def reverse(self):
        if self.length == 0:
            return "List is empty"
        if self.length == 1:
            return self
        current = self.head
        prev = None
        while (current):
            prev = current.prev
            current.prev = current.next
            current.next = prev
            current = current.prev
        self.head, self.tail = self.tail, self.head
        return self


l = DoublyLinkedList()

l.push(100)
l.push(10)
l.push(20)
l.push(50)
l.push(60)
l.push(70)
l.push(80)
l.traverse()
print('--------------------')
l.insert(3, 1)
l.traverse()
print("--------------------")
l.reverse()
print(l.pop().val)
print("--------------------")
l.unshift(1000000)
print("--------------------")
l.traverse()
