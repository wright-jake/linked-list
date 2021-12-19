#example input
head = [1,2,6,3,4,5,6], val = 6

#solution
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        
        #initialise a dummy pointer to avoid dealing with any issues if value of head is equal to target value
        dummy = ListNode(0)
        dummy.next = head
        
        #initialise pointers
        curr, prev = head, dummy
        
        #while current pointer is valid
        while curr:
            
            #check to see if node value is equal to target value
            if curr.val == val:
                
                #if it is change the references of the nodes either side
                prev.next = curr.next
            
            #otherwise increment the pointers
            else:
                prev = curr
            curr = curr.next
        
        #return the list (everything after the dummy node)
        return dummy.next
