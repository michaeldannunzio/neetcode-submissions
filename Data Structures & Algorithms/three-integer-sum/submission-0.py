class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        for index, value in enumerate(nums):
            if index > 0 and value == nums[index - 1]:
                continue
            left = index + 1
            right = len(nums) - 1
            while left < right:
                triplets = [value, nums[left], nums[right]]
                if sum(triplets) > 0:
                    right -= 1
                elif sum(triplets) < 0:
                    left += 1
                else:
                    result.append(triplets)
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1

        return result
        