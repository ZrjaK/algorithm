# 题目：886.可能的二分法
# 难度：MEDIUM
# 最后提交：2022-10-16 00:02:50 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        d = defaultdict(list)
        for i, j in dislikes:
            d[i].append(j)
            d[j].append(i)
        visited = set()
        color = [False] * (n+1)
        for i in range(1, n+1):
            if i in visited:
                continue
            q = deque([i])
            while q:
                t = q.popleft()
                if t in visited:
                    continue
                visited.add(t)
                for nxt in d[t]:
                    if nxt in visited and color[nxt] == color[t]:
                        return False
                    color[nxt] = not color[t]
                    q.append(nxt)
        return True