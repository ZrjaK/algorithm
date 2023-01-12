# 题目：面试题67.把字符串转换成整数
# 难度：MEDIUM
# 最后提交：2022-10-03 21:17:27 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def strToInt(self, str: str) -> int:
        return max(min(int(*re.findall('^[\+\-]?\d+', str.lstrip())), 2**31 - 1), -2**31)