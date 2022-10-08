# 题目：811.子域名访问计数
# 难度：MEDIUM
# 最后提交：2022-10-05 00:19:52 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        d = defaultdict(int)
        for c, u in [i.split(" ") for i in cpdomains]:
            f = u.split(".")
            c = int(c)
            for i in range(len(f)):
                d[".".join(f[-i:])] += c
        return [f'{j} {i}' for i, j in d.items()]