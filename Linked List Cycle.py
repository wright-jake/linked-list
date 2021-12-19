#example input
head = [3,2,0,-4], pos = 1

#solution
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        #if head has a null value then there cannot be a cycle
        if head is None:
            return False
        
        #initialise pointers
        slow, fast = head, head.next
        
        #if there is a cycle then there will come a point where the slow and fast pointers are equal to each other
        while slow != fast:
            
            #if fast is about to go past the tail then there cannot be a cycle
            if fast is None or fast.next is None:
                return False
            
            #increment pointers
            slow = slow.next
            fast = fast.next.next
        
        #true when slow and fast pointers are equal to each other
        return True
