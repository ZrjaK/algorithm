# 题目：剑指 Offer II 114.外星文字典
# 难度：HARD
# 最后提交：2022-10-10 21:42:46 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def alienOrder(self, words: List[str]) -> str:
        g = defaultdict(list)
        inDeg = {c: 0 for c in words[0]}
        for s, t in pairwise(words):
            for c in t:
                inDeg.setdefault(c, 0)
            for u, v in zip(s, t):
                if u != v:
                    g[u].append(v)
                    inDeg[v] += 1
                    break
            else:
                if len(s) > len(t):
                    return ""

        q = [u for u, d in inDeg.items() if d == 0]
        for u in q:
            for v in g[u]:
                inDeg[v] -= 1
                if inDeg[v] == 0:
                    q.append(v)
        return ''.join(q) if len(q) == len(inDeg) else ""