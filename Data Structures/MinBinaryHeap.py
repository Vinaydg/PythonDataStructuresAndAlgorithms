class MinBinaryHeap:
    def __init__(self):
        self.values = []

    def insert(self, val):
        self.values.append(val)
        if len(self.values) == 1:
            return self
        index = len(self.values) - 1
        while index > 0:
            parentIndex = (index - 1) // 2
            parent = self.values[parentIndex]
            if val >= parent:
                break
            self.values[parentIndex], self.values[index] = val, parent
            index = parentIndex
        return self

    def extractMin(self):
        if len(self.values) == 0:
            return "Heap is Empty"
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
                if leftChild < ele:
                    swap = left
            if right < length:
                rightChild = self.values[right]
                if (swap == None and rightChild < ele) or (swap != None and rightChild < leftChild):
                    swap = right
            if swap is None:
                break
            self.values[index] = self.values[swap]
            self.values[swap] = ele
            index = swap


l = MinBinaryHeap()
l.insert(10)
l.insert(20)
l.insert(15)
l.insert(12)
l.insert(2)
l.insert(30)
l.insert(50)
l.insert(11)
print(l.values)
l.extractMin()
print(l.values)
l.extractMin()
print(l.values)
l.extractMin()
print(l.values)
l.extractMin()
