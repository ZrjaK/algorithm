# 题目：367.有效的完全平方数
# 难度：EASY
# 最后提交：2021-10-21 19:05:36 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        for i in range(1, num+1, 2):
            num -= i
            if num <= 0:
                break
        return num == 0
