class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l, r = 0, n-1
        i = (r - l) // 2
        print(l, r, i)
        
        return -1