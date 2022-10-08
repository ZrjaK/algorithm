# 题目：1884.鸡蛋掉落-两枚鸡蛋
# 难度：MEDIUM
# 最后提交：2022-07-21 01:52:44 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def twoEggDrop(self, n: int) -> int:
        @cache
        def p(i):
            if i == 1 or i == 2:
                return i
            res = 1e99
            for j in range(1, i+1):
                res = min(res, 1 + max(j-1, p(i-j)))
            return res
        return p(n)