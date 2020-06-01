class TreeComparator(object):
    
    def compare_trees(self, node1, node2):
        
        if not node1 or not node2: #example node1==None
            return node1 == node2
        
        if node1.data is not node2.data:
            return False
        
        return self.compare_trees(node1.leftChild, node2.leftChild) and self.compare_trees(node1.rightChild, node2.rightChild)

class Node(object):
    
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

class BinarySearchTree(object):

    def __init__(self):
        self.root = None

    def insert(self, data):
        if not self.root:
            self.root = Node(data)
        else:
            self.insertNode(data, self.root)

    #O(logN)
    def insertNode(self, data, node):

        if data < node.data:
            if node.leftChild:
                self.insertNode(data, node.leftChild)

            else:
                node.leftChild = Node(data)

        else:
            if node.rightChild:
                self.insertNode(data, node.rightChild)
            else:
                node.rightChild = Node(data)

if __name__ == "__main__":
    bst1 = BinarySearchTree()
    bst1.insert(10)
    bst1.insert(13)
    bst1.insert(2)
    bst1.insert(14)

    bst2 = BinarySearchTree()
    bst2.insert(10)
    bst2.insert(13)
    bst2.insert(2)
    bst2.insert(14)
   
    comparator = TreeComparator()
    print(comparator.compare_trees(bst1.root, bst2.root))
