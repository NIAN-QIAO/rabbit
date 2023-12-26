from typing import List
# list.sort() 方法会直接修改原列表，如果你希望保留原列表的顺序，可以使用 sorted() 函数，它会返回一个新的排好序的列表。
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return max(nums)
        sort_nums = sorted(nums)
        count = 1
        for i in range(len(nums)-2, -1, -1):
            if sort_nums[i] != sort_nums[i + 1]:
                count += 1
                if count == 3:
                    return sort_nums[i]
        if count != 3:
            return max(nums)
        # return sorted(set(nums))[-3]  if len(set(nums)) >= 3 else max(nums)
if __name__ == '__main__':
    a = Solution()
    nums = [2, 2, 3, 1]
    print(a.thirdMax(nums))
