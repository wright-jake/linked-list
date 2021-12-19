#example input
[3,2,0,-4]
1

#solution
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        #initialise pointers
        slow, fast = head, head
        
        #while fast pointer and next fast pointer are valid
        while fast and fast.next:
            
            #increment pointers
            slow = slow.next
            fast = fast.next.next
            
            #if we detect a cycle
            if slow == fast:
                break
        
        #if we don't detect a cycle
        else:
            return None
        
        #create a new pointer we can use to find the node where the cycle begins
        new = head
        while new != fast:
            new = new.next
            fast = fast.next
            
        return new
