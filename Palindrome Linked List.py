#example input
head = [1,2,2,1]

#solution
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        #create empty array to store our values from the linked list
        nums = []
        
        #first value we will add is the head value
        current_node = head
        
        #iterate through the linked list
        while current_node is not None:
            
            #add node value to linked list
            nums.append(current_node.val)
            
            #increment current node by 1
            current_node = current_node.next
        
        #initialise pointers
        left, right = 0, len(nums) - 1
        
        #iterate through array
        while left < right:
            
            #check for palindrome
            if nums[left] == nums[right]:
                left += 1
                right -= 1
            else:
                return False
        return True
