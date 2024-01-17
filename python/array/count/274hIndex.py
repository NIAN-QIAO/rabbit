from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        left, r = 0, n
        while left < r:
            mid = (left + r + 1) // 2
            if sum(c >= mid for c in citations) >= mid:
                left = mid
            else:
                r = mid - 1
        return r
