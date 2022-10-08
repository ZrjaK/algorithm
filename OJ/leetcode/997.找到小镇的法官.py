# 题目：997.找到小镇的法官
# 难度：EASY
# 最后提交：2021-11-03 13:33:24 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trusts = [0] * (n + 1)
        for frm, to in trust:
            trusts[to] += 1
            trusts[frm] -= 1
        for person in range(1, n + 1):
            if trusts[person] == n - 1: return person
        return -1