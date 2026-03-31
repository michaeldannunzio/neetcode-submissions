class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        k_min = max(piles)
        l_ptr, r_ptr = 1, k_min
        while l_ptr <= r_ptr:
            k = (l_ptr + r_ptr) // 2
            t = sum([math.ceil(float(p) / k) for p in piles])
            if t <= h:
                k_min = k
                r_ptr = k - 1
            else:
                l_ptr = k + 1
        return k_min