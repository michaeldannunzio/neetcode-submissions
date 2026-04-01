# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        pos, n1 = 1, 0
        while l1:
            n1 += l1.val * pos
            l1 = l1.next
            pos *= 10

        pos, n2 = 1, 0
        while l2:
            n2 += l2.val * pos
            l2 = l2.next
            pos *= 10

        pos, s = 1, n1 + n2
        curr = res = ListNode()

        if s == 0:
            return res

        while s:
            rem = s % (pos*10)
            val = rem // pos
            curr.next = ListNode(val)
            s -= rem
            pos *= 10
            curr = curr.next

        return res.next
