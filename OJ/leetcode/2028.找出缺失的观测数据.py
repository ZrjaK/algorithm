# 题目：2028.找出缺失的观测数据
# 难度：MEDIUM
# 最后提交：2022-03-27 15:16:05 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        s = mean * (n + len(rolls)) - sum(rolls)
        if s < n or s > 6 * n:
            return []
        return [s // n + 1] * (s % n) + [s // n] * (n - s % n)