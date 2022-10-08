# 题目：796.旋转字符串
# 难度：EASY
# 最后提交：2021-10-24 13:01:05 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        return len(s) == len(goal) and goal in s + s