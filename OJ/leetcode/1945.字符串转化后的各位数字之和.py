# 题目：1945.字符串转化后的各位数字之和
# 难度：EASY
# 最后提交：2022-12-15 01:44:52 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def getLucky(self, s: str, k: int) -> int:
        s = "".join(str(ord(i)-96) for i in s)
        for _ in range(k):
            s = str(sum(int(i) for i in s))
        return int(s)