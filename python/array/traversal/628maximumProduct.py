from typing import List
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        st = sorted(nums)
        ans = [st[0]*st[1]*st[2], st[-1]*st[-2]*st[-3], st[0]*st[-1]*st[-2], st[-1]*st[1]*st[0]]
        return max(ans)