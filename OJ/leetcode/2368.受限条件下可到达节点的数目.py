# 题目：2368.受限条件下可到达节点的数目
# 难度：MEDIUM
# 最后提交：2022-08-07 10:34:08 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        d = defaultdict(list)
        r = set(restricted)
        for i, j in edges:
            d[i].append(j)
            d[j].append(i)
        q = deque([0])
        v = set()
        res = []
        while q:
            t = q.popleft()
            if t in v:
                continue
            v.add(t)
            res.append(t)
            for nxt in d[t]:
                if nxt not in r:
                    q.append(nxt)
        return len(res)