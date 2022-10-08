# 题目：207.课程表
# 难度：MEDIUM
# 最后提交：2022-07-27 03:04:45 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        edges = defaultdict(list)
        indeg = [0] * numCourses

        for i, j in prerequisites:
            edges[j].append(i)
            indeg[i] += 1
        
        q = deque([u for u in range(numCourses) if indeg[u] == 0])
        visited = 0

        while q:
            visited += 1
            u = q.popleft()
            for v in edges[u]:
                indeg[v] -= 1
                if indeg[v] == 0:
                    q.append(v)

        return visited == numCourses