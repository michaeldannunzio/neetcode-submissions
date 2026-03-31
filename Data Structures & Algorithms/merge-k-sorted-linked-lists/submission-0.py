import heapq
import functools

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __lt__(self, node: ListNode) -> bool:
        return self.val < node.val

class Solution:    
    def mergeKLists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None

        head = cur = ListNode(0)
        heap = []
        for node in lists:
            if node:
                heapq.heappush(heap, node)

        while heap:
            node = heapq.heappop(heap)
            cur.next = node
            cur = cur.next
            node = node.next
            if node:
                heapq.heappush(heap, node)
        
        return head.next