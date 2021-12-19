#example input
head = [1,2,3,4,5], n = 2

#solution
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #dummy node before the head node as we want the node before n
        dummy = ListNode(0,head)
        
        #initialise left and right pointers
        left = dummy
        right = head 
        
        #we want to move the right pointer so it is starts from nth node from the start of the list
        while n > 0 and right:
            right = right.next
            n -= 1
            
        #we now want to increment the left and right nodes at the same pace and amount until the right pointer is at the end of the list, so then the left pointer will be 1 before the nth node (from the end of the list)
        while right:
            left = left.next
            right = right.next
            
        #now we want to delete the node, to do this we will change the mapping of the node before the nth node
        left.next = left.next.next
        
        #return linked list with removed node
        return dummy.next
