class Node(object):

    def __init__(self, data):
        self.data = data;
        self.nextNode = None;
        
class LinkedList(object):

    def __init__(self):
        self.head = None;
        self.size = 0;
        
    def get_middle_node(self):
        slow_pointer = self.head
        fast_pointer = self.head
        
        while fast_pointer.nextNode and fast_pointer.nextNode.nextNode:
            fast_pointer = fast_pointer.nextNode.nextNode
            slow_pointer = slow_pointer.nextNode
        
        
        return slow_pointer

    #O(1)
    def insertStart(self, data):

        self.size += 1;
        newNode = Node(data);

        if not self.head:
            self.head = newNode;
        else:
            newNode.nextNode = self.head;
            self.head = newNode;
    
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
    linkedlist.insertStart(10);
    linkedlist.insertStart(11);
    linkedlist.insertStart(26);
    
    
    print(linkedlist.get_middle_node().data)
