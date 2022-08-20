class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def push(self, val):
        newNode = Node(val)
        if self.length == 0:
            self.head = newNode
            self.tail = self.head
        else:
            self.tail.next = newNode
            self.tail = newNode
        self.length += 1
        return self

    def traverse(self):
        current = self.head
        while current:
            print(current.val)
            current = current.next

    def pop(self):
        if self.length == 0:
            return "List is Empty"
        current = self.head
        newTail = current
        while current.next:
            newTail = current
            current = current.next
        self.tail = newTail
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return current

    def shift(self):
        if self.length == 0:
            return "The list is empty"
        current = self.head
        newHead = self.head.next
        self.head = newHead
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return current

    def unshift(self, val):
        newHead = Node(val)
        if self.length == 0:
            self.head = newHead
            self.tail = self.head
        else:
            newHead.next = self.head
            self.head = newHead
        self.length += 1
        return self

    def get(self, index):
        if index >= self.length or index < 0:
            return None
        l = 0
        current = self.head
        while l < index:
            current = current.next
            l += 1
        return current

    def setval(self, val, index):
        node = self.get(index)
        if node is None:
            return False
        node.val = val
        return True

    def insert(self, val, index):
        insertingNode = Node(val)
        if 0 > index > self.length:
            return False
        if index == 0:
            self.unshift(val)
            return True
        if index == self.length:
            self.push(val)
            return True
        previousNode = self.get(index - 1)
        insertingNode.next = previousNode.next
        previousNode.next = insertingNode
        self.length += 1
        return True

    def remove(self, index):
        if 0 >= index >= self.length:
            return "Index is out of bound"
        if index == 0:
            return self.shift()
        if index == self.length - 1:
            return self.pop()
        previousNode = self.get(index - 1)
        removedNode = previousNode.next
        previousNode.next = removedNode.next
        return removedNode

    def reverse(self):
        current = self.head
        self.head = self.tail
        self.tail = current
        prev = None
        nex = None
        for i in range(self.length):
            nex = current.next
            current.next = prev
            prev = current
            current = nex
        return self


l = SinglyLinkedList()
l.push("We")
l.push("are")
l.push("the future")
l.push("of India.")
l.get(3)
l.setval("change", 3)
l.traverse()
print("--------------------")
l.reverse()
l.traverse()
