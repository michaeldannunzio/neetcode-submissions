class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numCount: dict[int, int] = {}

        for num in nums:
            if num not in numCount:
                numCount[num] = 0
            print(f"num [{num}]: {numCount[num]} -> {numCount[num] + 1}")
            numCount[num] += 1

        # remap dictionary keys -> values and values -> keys
        # get list of dictionary keys
        # sort list in descending order
        # select first k elements
        # for each element return the original key

        countSwapped = { count: num for num, count in numCount.items() }
        countListDesc = sorted(list(countSwapped.keys()), reverse=True)
        res = []

        print(f"countSwapped: {countSwapped}")
        print(f"countListDesc: {countListDesc}")
        for i in range(k):
            print(f"i: {i}")
            count = countListDesc[i]
            num = countSwapped[count]
            res.append(num)
        
        return res
