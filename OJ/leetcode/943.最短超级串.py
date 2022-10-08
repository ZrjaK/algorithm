# 题目：943.最短超级串
# 难度：HARD
# 最后提交：2022-09-22 22:51:27 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def shortestSuperstring(self, words: List[str]) -> str:
        m = len(words)
        @cache
        def p(state, pre):
            if state == (1<<m)-1:
                return pre
            res = "a" * 300
            for i in range(m):
                if state>>i & 1:
                    continue
                n = len(words[i])
                f = p(state|1<<i, words[i])
                for j in range(n, -1, -1):
                    if pre.endswith(words[i][:j]):
                        t = pre + f[j:]
                        if len(t) < len(res):
                            res = t
            return res
        return p(0, "")