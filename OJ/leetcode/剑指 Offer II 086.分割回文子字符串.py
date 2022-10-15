# 题目：剑指 Offer II 086.分割回文子字符串
# 难度：MEDIUM
# 最后提交：2022-10-09 16:43:41 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        n = len(s)
        def p(i, h):
            if i == n:
                res.append(h)
            f = deepcopy(h)
            for j in range(i, n):
                t = s[i:j+1]
                if t == t[::-1]:
                    p(j+1, f + [t])
        p(0, [])
        return res