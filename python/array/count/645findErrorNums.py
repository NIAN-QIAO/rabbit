from typing import List


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        emptydict = {}
        for i in range(1, len(nums)+1):
            emptydict[i] = 0
        for x in nums:
            emptydict[x] += 1
        for a in range(1, len(nums)+1):
            if emptydict[a] == 0:
                loss = a
            if emptydict[a] == 2:
                repeat = a
        return [repeat, loss]
