# 题目：882.细分图中的可到达结点
# 难度：HARD
# 最后提交：2022-09-28 14:58:50 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def reachableNodes(self, edges: List[List[int]], maxMoves: int, n: int) -> int:
        d = defaultdict(list)
        c = defaultdict(int)
        for i, j, k in edges:
            d[i].append(j)
            d[j].append(i)
            c[i, j] = k + 1
            c[j, i] = k + 1
        ans = 0
        pq = [(0, 0)]
        dst = [1e99] * n
        dst[0] = 0
        while pq:
            s, t = heappop(pq)
            for nxt in d[t]:
                if dst[t] + c[t, nxt] < dst[nxt]:
                    dst[nxt] = dst[t] + c[t, nxt]
                    heappush(pq, (dst[nxt], nxt))
        ans = len([i for i in dst if i <= maxMoves])
        for i, j, k in edges:
            if dst[i] > maxMoves and dst[j] > maxMoves:
                continue
            i2j = min(max(0, maxMoves - dst[i]), k)
            j2i = min(max(0, maxMoves - dst[j]), k)
            ans += min(i2j+j2i, k)
        return ans