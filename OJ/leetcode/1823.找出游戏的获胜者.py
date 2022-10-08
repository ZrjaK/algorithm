# 题目：1823.找出游戏的获胜者
# 难度：MEDIUM
# 最后提交：2022-05-04 13:59:23 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        q = deque([i for i in range(1,n+1)])
        for i in range(1,n):
            for j in range(1,k):
                q.append(q.popleft())
            q.popleft()
        return q.popleft()
        