# 题目：306.累加数
# 难度：MEDIUM
# 最后提交：2022-09-14 11:25:26 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)
        @cache
        def p(x, i, j):
            if j == n:
                return True
            for k in range(j+1, n+1):
                if str(int(num[x:i])) == num[x:i] and str(int(num[i:j])) == num[i:j] and str(int(num[j:k])) == num[j:k] and int(num[x:i]) + int(num[i:j]) == int(num[j:k]):
                    if p(i, j, k):
                        return True
            return False
        res = False
        for i in range(1, n):
            for j in range(i+1, n):
                if p(0, i, j):
                    return True
        return False