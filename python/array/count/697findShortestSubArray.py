from typing import List
from collections import Counter


class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        dic = Counter()
        left, right = dict(), dict()
        for i, num in enumerate(nums):
            if num not in left:
                left[num] = i
            right[num] = i
            dic[num] += 1
        degree = max(dic.values())
        res = len(nums)
        for key, values in dic.items():
            if values == degree:
                res = min(res, right[key] - left[key] + 1)
        return res

        '''
        超时
        # degree, begin = 0, 0
        # end = len(nums) - 1
        # may = set()
        # for num in nums:
        #     if degree <= nums.count(num):
        #         degree = nums.count(num)
        # # print(degree)
        # for num in nums:
        #     if nums.count(num) == degree:
        #         may.add(num)
        # # print(may)
        # count = 0
        # result = float("inf")
        # for count in may:
        #     # print(count)
        #     while nums[begin] != count:
        #         begin += 1
        #     while nums[end] != count:
        #         end -= 1
        #     # print(begin, end)
        #     if end - begin + 1 < result:
        #         result = end - begin + 1
        #     begin = 0
        #     end = len(nums) - 1
        # return result
        '''


if __name__ == '__main__':
    nums = [1, 2, 2, 3, 1]
    a = Solution()
    print(a.findShortestSubArray(nums))
