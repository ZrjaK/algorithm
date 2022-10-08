# 题目：2320.统计放置房子的方式数
# 难度：MEDIUM
# 最后提交：2022-06-26 10:46:15 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def countHousePlacements(self, n: int) -> int:
        @cache
        def p(i):
            if i == 1:
                return 2
            if i == 2:
                return 3
            return p(i-1)+p(i-2)
        return p(n) ** 2 % int(1e9+7)