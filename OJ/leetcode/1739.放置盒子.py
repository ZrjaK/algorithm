# 题目：1739.放置盒子
# 难度：HARD
# 最后提交：2022-12-25 02:19:23 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def minimumBoxes(self, n: int) -> int:
        ans = 1
        a = 1
        while a < n:
            s = i = 0
            c = ans+1
            while a < n and s < c:
                i += 1
                s += i
                ans += 1
                a += i
        return ans