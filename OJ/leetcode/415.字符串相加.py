# 题目：415.字符串相加
# 难度：EASY
# 最后提交：2021-10-21 23:54:28 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i, j, carry, res = len(num1)-1, len(num2)-1, 0, 0
        ans = ''

        while i >= 0 or j >= 0 or carry != 0:
            val = carry

            if i >= 0:
                val += ord(num1[i]) - ord('0')
                i -= 1
            if j >= 0:
                val += ord(num2[j]) - ord('0')
                j -= 1

            carry, res = divmod(val, 10)
            ans = str(res) + ans

        return ans 