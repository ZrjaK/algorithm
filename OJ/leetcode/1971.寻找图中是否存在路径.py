# 题目：1971.寻找图中是否存在路径
# 难度：EASY
# 最后提交：2022-07-29 17:12:40 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        d = defaultdict(list)
        for i, j in edges:
            d[i].append(j)
            d[j].append(i)
        q = deque([source])
        visited = set()
        while q:
            cur = q.popleft()
            if cur == destination:
                return True
            if cur in visited:
                continue
            visited.add(cur)
            for nxt in d[cur]:
                q.append(nxt)
        return False