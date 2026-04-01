# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = cur = ListNode(None)
        ln1, ln2 = list1, list2

        while ln1 and ln2:
            cur.next = min(ln1, ln2, key=lambda ln: ln.val)
            cur = cur.next
            if ln1 == cur:
                ln1 = ln1.next
            else:
                ln2 = ln2.next
        cur.next = ln1 or ln2
        
        return head.next
