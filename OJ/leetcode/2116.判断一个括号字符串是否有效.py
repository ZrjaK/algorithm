# 题目：2116.判断一个括号字符串是否有效
# 难度：MEDIUM
# 最后提交：2022-09-05 10:21:18 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s) % 2:
            return False
        x = 0
        for i, j in zip(s, locked):
            if i == "(" or j == "0":
                x += 1
            elif x:
                x -= 1
            else:
                return False
        x = 0
        for i, j in zip(s[::-1], locked[::-1]):
            if i == ")" or j == "0":
                x += 1
            elif x:
                x -= 1
            else:
                return False
        return True