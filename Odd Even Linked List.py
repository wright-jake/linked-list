#example input
head = [1,2,3,4,5]

#solution
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        #if there is less than 3 nodes there is no point reordering
        if not head or not head.next or not head.next.next:
            return head
        
        #initialise pointers
        #we will start off with the head of the list being odd
        oddptr = curr = head
        
        #store the second node as the head of the even numbers so we can refer to this later
        evenptr = evenhead = head.next
        
        #index
        i = 1
        
        #checking if each node is even or odd
        while curr:
            
            #if odd
            if i > 2 and i % 2 != 0:
                
                #the odd pointer will point to our current node
                oddptr.next = curr
                
                #the odd pointer will now look at this odd node
                oddptr = oddptr.next
            
            #if even
            elif i > 2 and i % 2 == 0:
                
                #the even pointer will point to our current node
                evenptr.next = curr
                
                #the even pointer will now look at this even node
                evenptr = evenptr.next
            
            #increment node by 1
            curr = curr.next
            
            #increment index by 1
            i+= 1
        
        #we want the even list to end our linked list so the last even node will be the tail
        evenptr.next = None
        
        #the last odd node will point to the start of our even list
        oddptr.next = evenhead
        
        #return linked list
        return head
