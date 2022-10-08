# 题目：1864.构成交替字符串需要的最小交换次数
# 难度：MEDIUM
# 最后提交：2022-09-08 10:41:29 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def minSwaps(self, s: str) -> int:
        c = Counter(s)
        if abs(c["1"]-c["0"]) > 1:
            return -1
        m = ""
        if c["1"] > c["0"]:
            m = "10" * c["0"] + "1"
        elif c["1"] < c["0"]:
            m = "01" * c["1"] + "0"
        else:
            m = "01" * c["1"]
        return min(sum([1 for i, j in zip(s, m) if i != j]) // 2, 
                    sum([1 for i, j in zip(s, m[::-1]) if i != j]) // 2)
        