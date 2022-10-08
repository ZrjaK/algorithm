# 题目：2391.收集垃圾的最少总时间
# 难度：MEDIUM
# 最后提交：2022-08-28 10:46:08 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        n = len(garbage)
        ans = 0
        for a in ["G", "M", "P"]:
            l, r = 0, n-1
            # while l< n and a not in garbage[l]:
            #     l += 1
            while r >= 0 and a not in garbage[r]:
                r -= 1
            for i in range(l, r):
                ans += garbage[i].count(a) + travel[i]
            ans += garbage[r].count(a)
            # print(l, r, ans)
        return ans