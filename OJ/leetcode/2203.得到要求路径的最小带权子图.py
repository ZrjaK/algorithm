# 题目：2203.得到要求路径的最小带权子图
# 难度：HARD
# 最后提交：2022-10-11 14:40:31 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def minimumWeight(self, n: int, edges: List[List[int]], src1: int, src2: int, dest: int) -> int:
        d = defaultdict(set)
        f = defaultdict(set)
        c1 = defaultdict(lambda: 1e99)
        c2 = defaultdict(lambda: 1e99)
        for i, j, k in edges:
            d[i].add(j)
            f[j].add(i)
            c1[i, j] = min(c1[i, j], k)
            c2[j, i] = min(c2[j, i], k)
        def calc(z, o):
            dst = [1e99] * n
            dst[z] = 0
            pq = [[0, z]]
            b = f if o else d
            c = c2 if o else c1
            while pq:
                s, t = heappop(pq)
                for nxt in b[t]:
                    if s + c[t, nxt] < dst[nxt]:
                        dst[nxt] = s + c[t, nxt]
                        heappush(pq, [dst[nxt], nxt])
            return dst
        dst0 = calc(dest, True)
        dst1 = calc(src1, False)
        dst2 = calc(src2, False)
        # print(dst0, dst1, dst2)
        ans = 1e99
        for i in range(n):
            ans = min(ans, dst0[i] + dst1[i] + dst2[i])
        return ans if ans < 1e90 else -1