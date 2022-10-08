# 题目：693.交替位二进制数
# 难度：EASY
# 最后提交：2021-10-23 14:36:27 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        return not ('11' in bin(n) or '00' in bin(n))
        
