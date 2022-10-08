# 题目：1678.设计 Goal 解析器
# 难度：EASY
# 最后提交：2022-04-10 06:37:05 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def interpret(self, command: str) -> str:
        return command.replace("()","o").replace("(al)", "al")