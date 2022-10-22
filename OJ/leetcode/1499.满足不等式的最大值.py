# 题目：1499.满足不等式的最大值
# 难度：HARD
# 最后提交：2022-10-17 21:55:57 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        ans = -1e99
        q = deque()
        for x, y in points:
            while q and x-q[0][0] > k:
                q.popleft()
            if q and x != q[0][0]:
                ans = max(ans, y+x+q[0][1]-q[0][0])
            while q and q[-1][1]-q[-1][0] <= y - x:
                q.pop()
            q.append((x, y))
        return ans