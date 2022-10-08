# 题目：275.H 指数 II
# 难度：MEDIUM
# 最后提交：2022-04-25 10:36:58 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        l, r, ans = 0, len(citations)-1, 0
        while l <= r:
            mid = l+r>>1
            if len(citations)-mid > citations[mid]:
                l = mid + 1
            else:
                ans = len(citations) - mid
                r = mid - 1
        return ans