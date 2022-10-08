# 题目：1306.跳跃游戏 III
# 难度：MEDIUM
# 最后提交：2022-08-08 17:37:11 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        q = deque([start])
        v = set()
        while q:
            t = q.popleft()
            if t in v:
                continue
            v.add(t)
            if arr[t] == 0:
                return True
            if t + arr[t] < n:
                q.append(t + arr[t])
            if t - arr[t] >= 0:
                q.append(t - arr[t])
        return False