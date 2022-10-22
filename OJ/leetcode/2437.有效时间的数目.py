# 题目：2437.有效时间的数目
# 难度：EASY
# 最后提交：2022-10-15 22:49:03 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def countTime(self, time: str) -> int:
        t = time.split(":")
        ans = 1
        if t[0][0] == "?":
            if t[0][1] != "?":
                if t[0][1] <= "3":
                    ans *= 3
                else:
                    ans *= 2
            else:
                ans *= 24
        elif t[0][1] == "?":
            if t[0][0] in "01":
                ans *= 10
            else:
                ans *= 4
        
        if t[1][0] == "?":
            ans *= 6
        if t[1][1] == "?":
            ans *= 10
        return ans
        