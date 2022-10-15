# 题目：887.鸡蛋掉落
# 难度：HARD
# 最后提交：2022-10-11 21:02:28 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        @cache
        def calc(rest, j):
            if rest == 1 or j == 1:
                return j + 1
            return calc(rest-1, j-1) + calc(rest, j-1)
        for ans in range(1, n+1):
            if calc(k, ans) >= n+1:
                return ans