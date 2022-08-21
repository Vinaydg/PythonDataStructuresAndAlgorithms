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

    def DFSPreOrder(self):
        data = []
        current = self.root

        def traverse(node):
            data.append(node.val)
            if node.left:
                traverse(node.left)
            if node.right:
                traverse(node.right)

        traverse(current)
        return data

    def DFSPostOrder(self):
        data = []
        current = self.root

        def traverse(node):
            if node.left:
                traverse(node.left)
            if node.right:
                traverse(node.right)
            data.append(node.val)

        traverse(current)
        return data

    def DFSInOrder(self):
        data = []
        current = self.root

        def traverse(node):
            if node.left:
                traverse(node.left)
            data.append(node.val)
            if node.right:
                traverse(node.right)

        traverse(current)
        return data


bst = BinarySearchTree()
bst.insert(10)
bst.insert(6)
bst.insert(15)
bst.insert(3)
bst.insert(8)
bst.insert(20)
print(bst.DFSPreOrder())
print(bst.DFSPostOrder())
print(bst.DFSInOrder())