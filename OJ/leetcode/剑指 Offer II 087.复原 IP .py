# 题目：剑指 Offer II 087.复原 IP 
# 难度：MEDIUM
# 最后提交：2022-10-09 16:46:51 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        n = len(s)
        res = []
        def p(i, h):
            if i == n and len(h) == 4:
                res.append(".".join(h))
            if len(h) == 4:
                return
            f = deepcopy(h)
            for j in range(i, n):
                t = int(s[i:j+1])
                if str(t) == s[i:j+1] and 0 <= t <= 255:
                    p(j+1, f + [str(t)])
        p(0, [])
        return res