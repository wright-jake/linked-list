#example input
["MyLinkedList","addAtHead","addAtTail","addAtIndex","get","deleteAtIndex","get"]
[[],[1],[3],[1,2],[1],[1],[1]]

#solution
class Node:

    def __init__(self, val):
        self.val = val
        self.next = None


class MyLinkedList:

    def __init__(self):
        #first we will create the linked list data structure, currently it has a head node with an empty value and size 0
        self.head = None
        self.size = 0

        
    def get(self, index: int) -> int:
        #if index provided is invalid return -1
        if index < 0 or index >= self.size:
            return -1
        
        #if head is null then there are no values to take from list
        if self.head is None:
            return -1
        
        #start from beginning of list where curr is current node
        curr = self.head
        
        #increment node until we reach the node with the index provided
        for i in range(index):
            curr = curr.next
        
        #return value of node when it is at the index
        return curr.val
       
        
    def addAtHead(self, val):
        self.addAtIndex(0, val)

        
    def addAtTail(self, val):
        self.addAtIndex(self.size, val)
    
    
    def addAtIndex(self, index, val):
        #if index is out of range return -1
        if index < 0 or index > self.size:
            return 
        
        #create a new node
        node = Node(val)
        
        #add a new node at the head
        if index == 0:
            
            #increment the node by 1 and then give it the value and reference of the previous head node
            node.next = self.head
            
            #change the head of the linked list to our new node
            self.head = node
            
        else:
            
            #curr is current node, we will start from the head of the list
            curr = self.head
            
            #if head of list has a null value then the current node will become the head of the list
            if curr is None:
                self.head = node
            
            else:
                #we will iterate current node through list and insert it before the index provided node
                for i in range(index - 1):
                    curr = curr.next
                node.next = curr.next
                curr.next = node
        
        #as we add new node we need to increment the size by 1
        self.size += 1
      
    
    def deleteAtIndex(self, index: int) -> None:
        #check if index is valid
        if index < 0 or index >= self.size:
            return
        
        #curent node will begin from the head of the list
        curr = self.head
        
        #if index is 0 we will be deleting the node at the head
        if index == 0:
            self.head = curr.next
            
        else:
            for i in range(index - 1):
                curr = curr.next
            curr.next = curr.next.next
        
        #size of list will decrease by 1 as we are deleting a node
        self.size -= 1

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
