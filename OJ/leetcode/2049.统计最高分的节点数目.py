# 题目：2049.统计最高分的节点数目
# 难度：MEDIUM
# 最后提交：2022-08-20 16:14:54 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        n = len(parents)
        h = []
        d = defaultdict(list)
        for i, j in enumerate(parents):
            d[j].append(i)
        def p(i):
            t = []
            for c in d[i]:
                t.append(p(c))
            if t:
                h.append(t)
                return 1 + sum(t)
            h.append([0, 0])
            return 1
        s = p(0)
        ans = 1
        c = -1
        for i in h:
            t = s-sum(i)-1
            if t <= 0:
                t = 1
            for j in i:
                if j:
                    t *= j
            if c == t:
                ans += 1
            elif c < t:
                c = t
                ans = 1
        return ans