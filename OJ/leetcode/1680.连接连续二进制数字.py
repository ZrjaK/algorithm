# 题目：1680.连接连续二进制数字
# 难度：MEDIUM
# 最后提交：2022-04-10 06:42:11 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def concatenatedBinary(self, n: int) -> int:
        return int("".join([bin(i)[2:] for i in range(1,n+1)]), 2) % int(1e9+7)