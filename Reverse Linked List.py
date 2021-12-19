#example input
head = [1,2,3,4,5]

#solution
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #initialise pointers
        prev, curr = None, head
        
        #we will reverse the list until the next node is null
        while curr:
            
            #stores the next node in the list to reverse
            nxt = curr.next
            
            #reverse the node - basically we want to change direction the node is pointing
            curr.next = prev
            
            #then we will set the new previous node as the node we just changed the direction of
            prev = curr
            
            #we will change the reversed node to the next node to reverse
            curr = nxt
        
        #return the reversed list
        return prev
