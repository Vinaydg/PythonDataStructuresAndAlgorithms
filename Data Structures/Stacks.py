class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class Stack:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def push(self, val):
        newNode = Node(val)
        if self.length == 0:
            self.first = newNode
            self.last = newNode
            self.length += 1
            return self.length
        newNode.next = self.last
        self.last = newNode
        self.length += 1
        return self.length

    def pop(self):
        if self.length == 0:
            return None
        popNode = self.last
        if self.length == 1:
            self.last = None
            self.first = None
            self.length -= 1
            popNode.next = None
            return popNode.val
        self.last = popNode.next
        popNode.next = None
        self.length -= 1
        return popNode.val


stack = Stack()
stack.push(100)
stack.push(200)
stack.push(300)
stack.push(500)
print("-----------------------")
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())