#example input
head = [1,2,3,4,5]

#solution
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #slow and fast pointers start from head of list
        slow = fast = head
        
        #we want to continue loop while fast pointer and fast pointer incremented by 1 are still valid
        while fast and fast.next:
            
            #increment slow pointer by 1
            slow = slow.next
            
            #increment fast pointer by 2
            fast = fast.next.next
        
        #when the while loop is no longer valid then we have reached the end of the list, at this point the slow pointer has incremented half the amount so it will be at the middle node
        return slow
