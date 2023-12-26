from typing import List
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        i = 0
        count = 0
        max = 0
        while i < len(nums):
            if nums[i] != 1:
                if max < count:
                    max = count
                count = 0
                i += 1
            else:
                count += 1
                i += 1
        if max < count:
            max = count
        return max
if __name__ == '__main__':
    a=Solution()
    nums=[1,0,1,1,0,1]
    print(a.findMaxConsecutiveOnes(nums))
