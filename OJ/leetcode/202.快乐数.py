# 题目：202.快乐数
# 难度：EASY
# 最后提交：2021-10-21 11:15:46 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def isHappy(self, n: int) -> bool:
        res = []
        while 1:
            n = sum([ int(i)**2 for i in str(n)])
            if n == 1:
                return True
            else:
                if n not in res:
                    res.append(n)
                else:
                    return False