# 题目：2246.相邻字符不同的最长路径
# 难度：HARD
# 最后提交：2022-09-20 09:30:23 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        n = len(parent)
        d = defaultdict(list)
        for i in range(1, n):
            d[parent[i]].append(i)

        ans = 0
        def dfs(x: int) -> int:
            nonlocal ans
            max_len = 0
            for y in d[x]:
                l = dfs(y) + 1
                if s[y] != s[x]:
                    ans = max(ans, max_len + l)
                    max_len = max(max_len, l)
            return max_len
        dfs(0)
        return ans + 1