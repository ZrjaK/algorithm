# 题目：2275.按位与结果大于零的最长组合
# 难度：MEDIUM
# 最后提交：2022-05-15 10:45:49 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        d = defaultdict(list)
        for i in candidates:
            for j in range(32):
                if 1 & (i>>j) == 1:
                    d[j].append(i)
        ans = 0
        for i in d.values():
            ans = max(ans, len(i))
        return ans