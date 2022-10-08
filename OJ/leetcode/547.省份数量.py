# 题目：547.省份数量
# 难度：MEDIUM
# 最后提交：2022-07-29 02:52:11 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = set()
        ans = 0
        for i in range(n):
            if i in visited:
                continue
            q = deque([i])
            while q:
                j = q.popleft()
                if j in visited:
                    continue
                visited.add(j)
                for k in range(n):
                    if isConnected[j][k]:
                        q.append(k)
            ans += 1
        return ans