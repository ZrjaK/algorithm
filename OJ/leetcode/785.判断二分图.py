# 题目：785.判断二分图
# 难度：MEDIUM
# 最后提交：2022-08-01 17:33:44 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        color = [False] * n
        visited = set()
        for i in range(n):
            if i in visited:
                continue
            q = deque([i])
            while q:
                t = q.popleft()
                if t in visited:
                    continue
                visited.add(t)
                for nxt in graph[t]:
                    if nxt in visited and color[nxt] == color[t]:
                        return False
                    color[nxt] = not color[t]
                    q.append(nxt)
        return True