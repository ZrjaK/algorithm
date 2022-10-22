# 题目：1323.6 和 9 组成的最大数字
# 难度：EASY
# 最后提交：2022-10-20 16:13:42 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def maximum69Number (self, num: int) -> int:
        s = list(str(num))
        ans = num
        for i in range(len(s)):
            if s[i] == "6":
                s[i] = "9"
                ans = max(ans, int("".join(s)))
                s[i] = "6"
        return ans