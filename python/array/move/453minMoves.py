from typing import List


class Solution:
    def minMoves(self, nums: List[int]) -> int:
        # 题意可理解位每次让一个值减去1，使得所有的值相等，那理想情况就是每个值最终等于最小值。
        minvalue = min(nums)
        res = 0
        for num in nums:
            res += abs(num - minvalue)
        return res


if __name__ == '__main__':
    nums = [4, 3, 2, 7, 8, 2, 3, 1]
    a = Solution()
    print(a.findDisappearedNumbers(nums))
