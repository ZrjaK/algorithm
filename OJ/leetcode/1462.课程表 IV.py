# 题目：1462.课程表 IV
# 难度：MEDIUM
# 最后提交：2022-08-11 07:45:27 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # 建图，统计各节点入度
        g = defaultdict(list)
        indeg = defaultdict(int)
        for u, v in prerequisites:
            g[u].append(v)
            indeg[v] += 1

        # 将入度为0的点压栈
        stack = list()
        for i in range(numCourses):
            if not indeg[i]:
                stack.append(i)

        # 每次将一个入度为0的点从图上去除，更新子节点的入度，更新子节点的祖先表，将入度为0的子节点压栈
        father = [set() for _ in range(numCourses)]
        while stack:
            u = stack.pop()
            for v in g[u]:
                father[v].add(u)
                father[v].update(father[u])
                indeg[v] -= 1
                if not indeg[v]:
                    stack.append(v)
        
        # 根据祖先表判断课程先修情况
        ans = [False]*len(queries)
        for i, (u, v) in enumerate(queries):
            if u in father[v]:
                ans[i] = True
        
        return ans