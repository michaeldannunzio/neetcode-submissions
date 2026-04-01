# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        half2 = slow.next
        prev = slow.next = None
        while half2:
            swap = half2.next
            half2.next = prev
            prev = half2
            half2 = swap

        half1, half2 = head, prev
        while half2:
            swap1, swap2 = half1.next, half2.next
            half1.next = half2
            half2.next = swap1
            half1, half2 = swap1, swap2
