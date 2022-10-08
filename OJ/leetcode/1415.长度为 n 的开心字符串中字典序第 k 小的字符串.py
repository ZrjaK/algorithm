# 题目：1415.长度为 n 的开心字符串中字典序第 k 小的字符串
# 难度：MEDIUM
# 最后提交：2022-09-14 13:31:36 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        @cache
        def p(t, rest):
            if not rest:
                return [""]
            res = []
            for x in ["a", "b", "c"]:
                if x == t:
                    continue
                for j in p(x, rest-1):
                    res.append(x+j)
            return res
        h = sorted(p(0, n))
        return h[k-1] if k <= len(h) else ""