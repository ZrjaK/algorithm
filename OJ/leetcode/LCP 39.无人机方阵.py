# 题目：LCP 39.无人机方阵
# 难度：EASY
# 最后提交：2023-01-30 21:06:54 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def minimumSwitchingTimes(self, source: List[List[int]], target: List[List[int]]) -> int:
        c1 = defaultdict(int)
        for i in source:
            for j in i:
                c1[j] += 1
        c2 = defaultdict(int)
        for i in target:
            for j in i:
                c2[j] += 1
        for i in c1:
            c2[i] -= c1[i]
        ans = 0
        for i in c2.values():
            ans += abs(i)
        return ans // 2
