# Priority Queue / Heap
# Time: O(Nlogk)
# Space: O(n)
class ListNode:    
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __lt__(self, other):
        return self.val < other.val

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = current = ListNode(0)
        heapq.heapify(lists)
        while lists:
            node = heapq.heappop(lists)
            current.next = node
            current = current.next
            if node.next:
                heapq.heappush(lists, node.next)
        return dummy.next