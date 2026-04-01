# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        ref, count = ListNode(next=head), n
        left, right = ref, head
        while count > 0:
            right = right.next
            count -= 1
        
        while right:
            left, right = left.next, right.next

        left.next = left.next.next
        return ref.next
        