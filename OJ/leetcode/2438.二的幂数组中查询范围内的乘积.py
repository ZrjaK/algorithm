# 题目：2438.二的幂数组中查询范围内的乘积
# 难度：MEDIUM
# 最后提交：2022-10-15 23:51:20 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        arr = []
        for i in range(30):
            if n>>i & 1:
                arr.append(i)
        h = list(accumulate(arr))
        ans = []
        for l, r in queries:
            t = h[r]
            if l:
                t -= h[l-1]
            ans.append(pow(2, t, int(1e9+7)))
        return ans