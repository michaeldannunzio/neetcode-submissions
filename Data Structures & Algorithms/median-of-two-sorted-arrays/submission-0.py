class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        t = len(nums1) + len(nums2)
        h = t // 2

        a, b = nums1, nums2
        if len(b) < len(a):
            a, b = b, a

        l, r = 0, len(a) - 1
        while True:
            i = (l+r) // 2
            j = h-i-2

            la = a[i]   if i >= 0         else float('-inf')
            ra = a[i+1] if (i+1) < len(a) else float('inf')
            lb = b[j]   if j >= 0         else float('-inf')
            rb = b[j+1] if (j+1) < len(b) else float('inf')

            if la <= rb and lb <= ra:
                if t % 2:
                    return min(ra, rb)
                return (max(la,lb) + min(ra,rb)) / 2
            elif la > rb:
                r = i-1
            else:
                l = i+1
