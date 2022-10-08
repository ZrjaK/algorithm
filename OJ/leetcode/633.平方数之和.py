# 题目：633.平方数之和
# 难度：MEDIUM
# 最后提交：2022-04-26 19:40:18 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        j = int(math.sqrt(c))
        i = 0
        while i <= j:
            total = i * i + j * j
            if total > c:
                j = j - 1
            elif total < c:
                i = i + 1
            else:
                return True
        return False