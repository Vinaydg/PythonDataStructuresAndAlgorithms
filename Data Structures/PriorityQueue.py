class Node:
    def __init__(self, val, priority):
        self.val = val
        self.priority = priority


class PriorityQueue:
    def __init__(self):
        self.values = []

    def Enqueue(self, val, priority):
        node = Node(val, priority)
        self.values.append(node)
        if len(self.values) == 1:
            return self
        index = len(self.values) - 1
        while index > 0:
            parentIndex = (index - 1) // 2
            parent = self.values[parentIndex]
            if node.priority >= parent.priority:
                break
            self.values[parentIndex], self.values[index] = node, parent
            index = parentIndex
        return self

    def Dequeue(self):
        if len(self.values) == 0:
            return "Priority Queue is Empty"
        if len(self.values) == 1:
            return self.values.pop()
        minVal = self.values[0]
        end = self.values.pop()
        self.values[0] = end
        self.bubbleDown()
        return minVal

    def bubbleDown(self):
        index = 0
        length = len(self.values)
        ele = self.values[index]
        while True:
            left = 2 * index + 1
            right = 2 * index + 2
            leftChild = 0
            rightChild = 0
            swap = None
            if left < length:
                leftChild = self.values[left]
                if leftChild.priority < ele.priority:
                    swap = left
            if right < length:
                rightChild = self.values[right]
                if (swap == None and rightChild.priority < ele.priority) or (
                        swap != None and rightChild.priority < leftChild.priority):
                    swap = right
            if swap is None:
                break
            self.values[index] = self.values[swap]
            self.values[swap] = ele
            index = swap


l = PriorityQueue()
l.Enqueue(10, 1)
l.Enqueue(20, 5)
l.Enqueue(15, 3)
l.Enqueue(12, 4)
l.Enqueue(2, 7)
l.Enqueue(30, 10)
l.Enqueue(50, 11)
l.Enqueue(11, 22)
l.Enqueue(10, 2)
a = l.Dequeue()
print(a.val, a.priority)
a = l.Dequeue()
print(a.val, a.priority)
a = l.Dequeue()
print(a.val, a.priority)
a = l.Dequeue()
print(a.val, a.priority)
a = l.Dequeue()
print(a.val, a.priority)
a = l.Dequeue()
print(a.val, a.priority)
a = l.Dequeue()
print(a.val, a.priority)
a = l.Dequeue()
print(a.val, a.priority)
a = l.Dequeue()
print(a.val, a.priority)
