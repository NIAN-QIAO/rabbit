from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = -1
        for j in range(len(nums)):
            if nums[j] != 0:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]


if __name__ == '__main__':
    nums = [0, 0]
    a = Solution()
    a.moveZeroes(nums)
    print(nums)
