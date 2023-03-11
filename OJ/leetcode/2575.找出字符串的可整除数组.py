# 题目：2575.找出字符串的可整除数组
# 难度：MEDIUM
# 最后提交：2023-02-26 10:33:38 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def divisibilityArray(self, word: str, m: int) -> List[int]:
        ans = []
        s = 0
        for i in word:
            s = s * 10 + int(i)
            s %= m
            ans.append(int(s % m == 0))
        return ans