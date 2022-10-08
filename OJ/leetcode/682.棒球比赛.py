# 题目：682.棒球比赛
# 难度：EASY
# 最后提交：2021-10-23 14:02:29 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def calPoints(self, ops: List[str]) -> int:
        i = 0
        while i < len(ops):
            if ops[i] == "+":
                ops[i] = int(ops[i-2]) + int(ops[i-1])
            if ops[i] == "D":
                ops[i] = int(ops[i-1]) * 2
            if ops[i] == "C":
                del ops[i]
                del ops[i-1]              
                i -= 1
                continue
            ops[i] = int(ops[i])
            i += 1
        return sum(ops)
            