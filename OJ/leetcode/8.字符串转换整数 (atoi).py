# 题目：8.字符串转换整数 (atoi)
# 难度：MEDIUM
# 最后提交：2022-09-06 09:05:36 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def myAtoi(self, s: str) -> int:
        return max(min(int(*re.findall('^[\+\-]?\d+', s.lstrip())), 2**31 - 1), -2**31)