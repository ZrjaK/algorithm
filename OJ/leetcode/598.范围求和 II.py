# 题目：598.范围求和 II
# 难度：EASY
# 最后提交：2021-10-23 01:00:54 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        return min([a for a,_ in ops ]) * min([b for _,b in ops]) if ops else m * n