class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numCount: dict[int, int] = {}

        for num in nums:
            print("num:", num)
            if num not in numCount:
                numCount[num] = 0
            numCount[num] += 1

        # remap dictionary keys -> values and values -> keys
        # get list of dictionary keys
        # sort list in descending order
        # select first k elements
        # for each element return the original key

        countSwapped = { count: num for num, count in numCount.items() }
        countListDesc = sorted(list(countSwapped.keys()), reverse=True)
        res = []

        print(countSwapped)
        print(countListDesc)
        for i in range(k):
            print(i)
            count = countListDesc[i]
            num = countSwapped[count]
            res.append(num)
        
        return res
