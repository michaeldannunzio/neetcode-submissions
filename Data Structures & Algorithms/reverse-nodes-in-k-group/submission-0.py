# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        res = ListNode(0, head)
        curr = h1 = h2 = head
        n = 0
        while curr:
            if n < k:
                h2 = h2.next
            curr = curr.next
            n += 1

        curr, prev = h2, None
        while curr and n <= k:
            swap = curr.next
            curr.next = prev
            prev = curr
            curr = swap
        h2 = prev

        curr, prev = h1, None
        while curr:
            if curr.next.next == None:
                curr.next = None
            swap = curr.next
            curr.next = prev
            prev = curr
            curr = swap
        
        h1.next = h2
        h1 = prev

        return h1