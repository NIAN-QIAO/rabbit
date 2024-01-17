from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        length = len(nums)
        for i in range(0, length):
            num = abs(nums[i])
            if nums[num - 1] < 0:
                res.append(num)
            else:
                nums[num - 1] = -nums[num - 1]
        return res


if __name__ == '__main__':
    nums = [4, 3, 2, 7, 8, 2, 3, 1]
    a = Solution()
    print(a.findDuplicates(nums))
