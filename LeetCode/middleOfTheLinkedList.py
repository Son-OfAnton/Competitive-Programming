# 876. Middle of the Linked List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        size = 0
        
        while curr:
            curr = curr.next
            size += 1
        
        middle = size // 2
        curr = head
        index = 0
        
        while curr:
            if index == middle:
                return curr
            curr = curr.next
            index += 1
        
# A better solution        
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = slow = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow
                
