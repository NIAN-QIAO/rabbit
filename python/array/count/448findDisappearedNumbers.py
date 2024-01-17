from typing import List
# from collections import Counter


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res = []
        # 如何快速判断数字在数组中存在吗？
        # 可以使用 set 数据结构，它的查找时间复杂度可以降低到 O(1)。
        # 在列表里面用 if not in 好像时间复杂度会变高。
        counter = set(nums)
        for i in range(1, len(nums) + 1):
            if i not in counter:
                res.append(i)
        return res


if __name__ == '__main__':
    nums = [4, 3, 2, 7, 8, 2, 3, 1]
    a = Solution()
    print(a.findDisappearedNumbers(nums))
