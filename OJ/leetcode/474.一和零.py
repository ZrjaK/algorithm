# 题目：474.一和零
# 难度：MEDIUM
# 最后提交：2022-07-05 18:21:48 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        @cache
        def p(i, j, k):
            if i == len(strs):
                return 0
            zero = strs[i].count("0")
            one = strs[i].count("1")
            res = p(i+1, j, k)
            if j <= m-zero and k <= n-one:
                res = max(res, 1 + p(i+1, j+zero, k+one))
            return res
        return p(0, 0, 0)