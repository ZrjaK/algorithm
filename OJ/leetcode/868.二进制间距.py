# 题目：868.二进制间距
# 难度：EASY
# 最后提交：2021-10-25 16:21:02 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def binaryGap(self, n: int) -> int:
        gaps = [len(_) for _ in bin(n)[2:].split('1')[1:-1]]
        return max(gaps) + 1 if len(gaps) > 0 else 0