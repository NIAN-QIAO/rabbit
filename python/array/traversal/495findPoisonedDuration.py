from typing import List
class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        i, ans = 1, 0
        begin, end = timeSeries[0], timeSeries[0] + duration-1
        while i < len(timeSeries):
            if end >= timeSeries[i]:
                end = timeSeries[i]+duration-1
                i += 1
            else:
                ans += (end-begin+1)
                begin = timeSeries[i]
                end = timeSeries[i] + duration-1
                i += 1
        ans += (end - begin + 1)
        return ans
if __name__=='__main__':
    a = Solution()
    timeSeries = [1, 4]
    duration = 2
    print(a.findPoisonedDuration(timeSeries,duration))


