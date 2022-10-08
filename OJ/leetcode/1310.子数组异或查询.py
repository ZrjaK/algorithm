# 题目：1310.子数组异或查询
# 难度：MEDIUM
# 最后提交：2022-04-28 20:34:18 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        h = [0]
        for i in arr:
            h.append(h[-1] ^ i)
        res = []
        for l, r in queries:
            res.append(h[r+1] ^ h[l])
        return res