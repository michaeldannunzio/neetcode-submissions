class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numCount: dict[int, int] = {}

        for num in nums:
            if num not in numCount:
                numCount[num] = 0
            print(f"num [{num}]: {numCount[num]} -> {numCount[num] + 1}")
            numCount[num] += 1

        print(f"numCount: {numCount}")

        # remap dictionary keys -> values and values -> keys
        # get list of dictionary keys
        # sort list in descending order
        # select first k elements
        # for each element return the original key

        countNestedList = [ [count, num] for num, count in numCount.items() ]
        countNestedListDesc = sorted(countNestedList, key=lambda x: x[0], reverse=True)
        # print(f"countNestedList: {countNestedList}")
        # print(f"countNestedListDesc: {countNestedListDesc}")
        return [ num for count, num in countNestedListDesc[:k] ]
