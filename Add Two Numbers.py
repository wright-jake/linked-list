#example input
l1 = [2,4,3], l2 = [5,6,4]

#solution
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        #mod by 10 to make sure we get the unit part
        l3 = ListNode((l1.val + l2.val) % 10)
        
        #integer division to work out if we need to carry any 'tens' over to the next digit
        carry = (l1.val + l2.val) // 10
        
        #use as our pointer
        curr = l3
        
        #check that we haven't searched through all of the lists
        while l1.next and l2.next:
            
            #go to the next node
            l1 = l1.next
            l2 = l2.next
            
            #add the nodes together
            curr.next = ListNode((carry + l1.val + l2.val) % 10)
            carry = (carry + l1.val + l2.val) // 10
            
            #update our pointer to the new node we just made
            curr = curr.next
        
        #if l1 still has nodes to add
        while l1.next:
            l1 = l1.next
            
            curr.next = ListNode((carry + l1.val) % 10)
            carry = (carry + l1.val) // 10
            curr = curr.next
        
        #if l2 still has nodes to add
        while l2.next:
            l2 = l2.next
            
            curr.next = ListNode((carry + l2.val) % 10)
            carry = (carry + l2.val) // 10
            curr = curr.next
        
        #if the final digits add to greater than 9, then we will add a node with the value 1
        if carry > 0:
            curr.next = ListNode(1)
        
        #return sum of linked lists
        return l3
        
