#example input


#output
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        #initialise pointers
        first, second = headA, headB
        
        #while pointers are not pointing at the same node
        while first != second:
            
            #if first pointer is pointing to an empty node, set the first pointer to point to headB, otherwise increment the pointer
            first = headB if first is None else first.next
            
            #if second pointer is pointing to an empty node, set the second pointer to point to headA, otherwise increment the pointer
            second = headA if second is None else second.next
        
        #return intersection node value or null
        return first
