# 题目：剑指 Offer 46.把数字翻译成字符串
# 难度：MEDIUM
# 最后提交：2022-10-03 18:38:17 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def translateNum(self, num: int) -> int:
        s = str(num)
        n = len(s)
        @cache
        def p(i):
            if i == n:
                return 1
            if i > n:
                return 0
            if s[i] > "2" or s[i] == "0":
                return p(i+1)
            elif s[i] == "1":
                return p(i+1) + p(i+2)
            elif i+1 < n and s[i+1] <= "5":
                return p(i+1) + p(i+2)
            return p(i+1)
        return p(0)