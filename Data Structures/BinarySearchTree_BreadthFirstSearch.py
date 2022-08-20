class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.frequency = 0


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, val):
        newNode = Node(val)
        if self.root is None:

            self.root = newNode
            return self
        else:
            current = self.root
            while True:
                if newNode.val == current.val:
                    current.frequency += 1
                    return self
                if newNode.val > current.val:
                    if current.right is None:
                        current.right = newNode
                        return self
                    else:
                        current = current.right
                else:
                    if current.left is None:
                        current.left = newNode
                        return self
                    else:
                        current = current.left

    def find(self, val):
        if self.root is None:
            return False
        else:
            current = self.root
            while True:
                if val == current.val:
                    return current
                if val > current.val:
                    if current.right is None:
                        return False
                    else:
                        current = current.right
                else:
                    if current.left is None:
                        return False
                    else:
                        current = current.left

    def BFS(self):
        node = self.root
        queue = []
        visited = []
        queue.append(node)
        while len(queue):
            node = queue.pop(0)
            visited.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return visited


bst = BinarySearchTree()
bst.insert(20)
bst.insert(10)
bst.insert(30)
bst.insert(9)
bst.insert(11)
bst.insert(40)
bst.insert(29)
bst.BFS()