# 题目：2546.执行逐位运算使字符串相等
# 难度：MEDIUM
# 最后提交：2023-01-22 14:11:14 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def makeStringsEqual(self, s: str, target: str) -> bool:
        c1 = s.count("1")
        c2 = target.count("1")
        if (not c2 and c1) or (not c1 and c2):
            return False
        return True