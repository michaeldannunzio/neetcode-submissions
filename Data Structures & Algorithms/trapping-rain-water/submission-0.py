class Solution:
    def trap(self, height: List[int]) -> int:
        leftHeight = 0
        rightHeight = 0
        length = len(height)
        maxLeftHeight = [0] * length
        maxRightHeight = [0] * length

        for i in range(length):
            leftPointer = i
            rightPointer = -i - 1
            maxLeftHeight[leftPointer] = leftHeight
            maxRightHeight[rightPointer] = rightHeight
            leftHeight = max(leftHeight, height[leftPointer])
            rightHeight = max(rightHeight, height[rightPointer])

        area = 0
        for i in range(length):
            potential = min(maxLeftHeight[i], maxRightHeight[i])
            area += max(0, potential - height[i])

        return area
