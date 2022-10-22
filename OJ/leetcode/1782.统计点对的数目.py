# 题目：1782.统计点对的数目
# 难度：HARD
# 最后提交：2022-10-18 09:18:00 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def countPairs(self, n: int, edges: List[List[int]], queries: List[int]) -> List[int]:
        f = defaultdict(int)
        cnt = [0] * n
        for i, j in edges:
            i -= 1
            j -= 1
            cnt[i] += 1
            cnt[j] += 1
            if i > j:
                i, j = j, i
            f[i, j] += 1
        ans = [0] * len(queries)
        s = sorted(cnt)
        for i in s:
            for j in range(len(queries)):
                t = bisect_left(s, queries[j]-i+1)
                ans[j] += n-t
                if i * 2 > queries[j]:
                    ans[j] -= 1
        ans = [i//2 for i in ans]
        for (a, b), c in f.items():
            t = cnt[a] + cnt[b]
            for j in range(len(queries)):
                if t > queries[j] and t-c <= queries[j]:
                    ans[j] -= 1
        return ans