class Node(object):

    def __init__(self, data):
        self.data = data;
        self.nextNode = None;
        
class LinkedList(object):

    def __init__(self):
        self.head = None;
        self.size = 0;

    #O(1)
    def insertStart(self, data):

        self.size += 1;
        newNode = Node(data);

        if not self.head:
            self.head = newNode;
        else:
            newNode.nextNode = self.head;
            self.head = newNode;
            
    def reverse(self):
        
        currentNode = self.head
        previousNode = None
        
        while currentNode is not None:
            nextNode = currentNode.nextNode
            currentNode.nextNode = previousNode
            previousNode = currentNode
            currentNode = nextNode
        
        self.head = previousNode
    
    def traverseList(self):

        actualNode = self.head;

        while actualNode is not None:
            print("%d " % actualNode.data);
            actualNode = actualNode.nextNode;

if __name__ == "__main__":
    
    linkedlist = LinkedList();
    
    linkedlist.insertStart(12);
    linkedlist.insertStart(122);
    linkedlist.insertStart(3);
    linkedlist.insertStart(31);
    linkedlist.insertStart(10)
    linkedlist.insertStart(11);
    
    linkedlist.traverseList();
    
    linkedlist.reverse()
    print("Reverse list:")
    linkedlist.traverseList();
    