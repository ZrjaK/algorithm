# 题目：1545.找出第 N 个二进制字符串中的第 K 位
# 难度：MEDIUM
# 最后提交：2022-09-03 02:05:48 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        if n == 1:
            return "0"
        mid = 1<<n-1
        if k == mid:
            return "1"
        elif k < mid:
            return self.findKthBit(n-1, k)
        else:
            k = 2*mid - k
            res = self.findKthBit(n-1, k)
            if res == "1":
                return "0"
            return "1"