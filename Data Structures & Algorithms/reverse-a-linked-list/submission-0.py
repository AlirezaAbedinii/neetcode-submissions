# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        
        
        prev = None
        current = head
        # temp = head.next
        # result = []
        while current.next is not None:
            temp = ListNode(current.next.val, current.next.next)
            current.next = prev
            prev = ListNode(current.val, current.next)
            current = temp

        current.next = prev
        # while current is not None:
        # result.append(current)
            # current = current.next
        
        return current


            
        