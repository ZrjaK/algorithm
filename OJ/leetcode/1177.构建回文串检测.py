# 题目：1177.构建回文串检测
# 难度：MEDIUM
# 最后提交：2022-08-25 23:16:11 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        h = list(accumulate([1<<(ord(i)-97) for i in s], lambda x, y: x ^ y)) + [0]
        return [(h[r]^h[l-1]).bit_count() - k*2 < 2 for l, r, k in queries]