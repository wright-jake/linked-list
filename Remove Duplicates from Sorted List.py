#example input
head = [1,1,2]

#solution
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #if head has no value just return head as not possible to have duplicates
        if head == None:
            return head
        
        #initialise pointers
        current = head.next
        prev = head
        
        #while pointer has not reached end of list
        while current != None:
            
            #list is sorted so if two values next to each other are duplicates then change the nextreference
            if current.val == prev.val:
                prev.next = current.next
                current = current.next
            
            #if not duplicate then increment pointers
            else:
                current = current.next
                prev = prev.next
        
        #return linked list with no duplicates
        return head
