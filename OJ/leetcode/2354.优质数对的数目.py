# 题目：2354.优质数对的数目
# 难度：HARD
# 最后提交：2022-07-24 11:18:59 +0800 CST
# 语言：python3
# 作者：ZrjaK

from sortedcontainers import SortedList
class Solution:
    def countExcellentPairs(self, nums: List[int], k: int) -> int:
        b = defaultdict(int)
        for i in nums:
            c = 0
            for j in range(40):
                if 1<<j & i:
                    c += 1
            b[i] = c
        ans = 0
        s = SortedList()
        for i in set(nums):
            ans += (len(s)-s.bisect_left(k-b[i])) * 2
            s.add(b[i])
            if b[i] * 2 >= k:
                ans += 1 
            # print(ans ,s)
        return ans