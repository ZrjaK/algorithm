# 题目：1519.子树中标签相同的节点数
# 难度：MEDIUM
# 最后提交：2022-08-10 21:09:36 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        d = defaultdict(list)
        for i, j in edges:
            d[i].append(j)
            d[j].append(i)
        v = set()
        r = [0] * n
        def p(i):
            if i in v:
                return [0] * 26
            v.add(i)
            res = [0]* 26
            for c in d[i]:
                t = p(c)
                for a in range(26):
                    res[a] += t[a]
            res[ord(labels[i])-97] += 1
            r[i] = res[ord(labels[i])-97]
            return res
        p(0)
        return r
            