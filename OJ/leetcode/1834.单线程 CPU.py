# 题目：1834.单线程 CPU
# 难度：MEDIUM
# 最后提交：2022-09-01 01:27:47 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        n = len(tasks)
        indices = list(range(n))
        indices.sort(key=lambda x: tasks[x][0])

        ans = []
        pq = []
        t = 0
        i = 0
        
        for _ in range(n):
            if not pq:
                t = max(t, tasks[indices[i]][0])
            while i < n and tasks[indices[i]][0] <= t:
                heapq.heappush(pq, (tasks[indices[i]][1], indices[i]))
                i += 1
            f = heapq.heappop(pq)
            t += f[0]
            ans.append(f[1])
        
        return ans