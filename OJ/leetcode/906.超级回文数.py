# 题目：906.超级回文数
# 难度：HARD
# 最后提交：2022-09-21 10:58:25 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def superpalindromesInRange(self, left: str, right: str) -> int:
        left = int(left)
        right = int(right)
        def check(x):
            x = x**2
            if left <= x <= right:
                x = str(x)
                if x == x[::-1]:
                    return 1
            return 0
        ans = 0
        for i in range(10**5):
            s = str(i)
            ans += check(int(s+s[::-1]))
            ans += check(int(s+s[:-1][::-1]))
        return ans