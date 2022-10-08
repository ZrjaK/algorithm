# 题目：405.数字转换为十六进制数
# 难度：EASY
# 最后提交：2022-08-25 02:12:55 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def toHex(self, num: int) -> str:
        d = "0123456789abcdef"
        ans = ""
        num &= (1<<32)-1
        while num:
            ans = d[num%16] + ans
            num //= 16
        return ans if ans else "0"