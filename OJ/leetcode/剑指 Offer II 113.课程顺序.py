# 题目：剑指 Offer II 113.课程顺序
# 难度：MEDIUM
# 最后提交：2022-10-10 17:12:24 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        d = defaultdict(list)
        indegree = [0] * numCourses
        for i, j in prerequisites:
            d[j].append(i)
            indegree[i] += 1
        q = deque([i for i in range(numCourses) if not indegree[i]])
        v = set()
        ans = []
        while q:
            t = q.popleft()
            if t in v:
                continue
            v.add(t)
            ans.append(t)
            for nxt in d[t]:
                indegree[nxt] -= 1
                if not indegree[nxt]:
                    q.append(nxt)
        return ans if len(ans) == numCourses else []