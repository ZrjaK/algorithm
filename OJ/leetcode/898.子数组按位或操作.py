# 题目：898.子数组按位或操作
# 难度：MEDIUM
# 最后提交：2022-07-08 15:50:35 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def subarrayBitwiseORs(self, A: List[int]) -> int:
        cur, res = set(), set()
        for a in A:
            cur = {a | b for b in cur}
            cur.add(a)
            res |= cur
        return len(res)