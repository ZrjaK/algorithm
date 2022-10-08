# 题目：210.课程表 II
# 难度：MEDIUM
# 最后提交：2022-07-27 03:06:31 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        edges = defaultdict(list)
        indeg = [0] * numCourses

        for i, j in prerequisites:
            edges[j].append(i)
            indeg[i] += 1
        
        q = deque([u for u in range(numCourses) if indeg[u] == 0])

        res = []
        while q:
            u = q.popleft()
            res.append(u)
            for v in edges[u]:
                indeg[v] -= 1
                if indeg[v] == 0:
                    q.append(v)

        return res if len(res) == numCourses else []