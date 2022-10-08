# 题目：2053.数组中第 K 个独一无二的字符串
# 难度：EASY
# 最后提交：2022-05-18 21:58:38 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        c = Counter(arr)
        for i in arr:
            if c[i] == 1:
                k -= 1
            if k == 0:
                return i
        return ""