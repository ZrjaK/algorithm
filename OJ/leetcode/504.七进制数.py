# 题目：504.七进制数
# 难度：EASY
# 最后提交：2023-01-30 20:41:52 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def convertToBase7(self, num: int) -> str:
        sig = 0
        if num < 0:
            sig = 1
            num *= -1
        ans = []
        while num:
            ans.append(num % 7)
            num //= 7
        ans = "".join(map(str, ans[::-1]))
        if not ans:
            ans = "0"
        if sig:
            ans = "-" + ans
        return ans