from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        counter = set(nums)
        res = 1
        while 1:
            if res in counter:
                res += 1
            else:
                return res


if __name__ == '__main__':
    nums = [3, 4, -1, 1]
    a = Solution()
    print(a.firstMissingPositive(nums))
