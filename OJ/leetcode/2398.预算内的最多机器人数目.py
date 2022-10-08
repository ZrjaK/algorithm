# 题目：2398.预算内的最多机器人数目
# 难度：HARD
# 最后提交：2022-09-03 22:46:19 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def maximumRobots(self, chargeTimes: List[int], runningCosts: List[int], budget: int) -> int:
        h = list(accumulate(runningCosts)) + [0]
        q = deque([])
        n = len(chargeTimes)
        l = 0
        t = 0
        ans = 0
        for i in range(n):
            while q and chargeTimes[q[-1]] <= chargeTimes[i]:
                q.pop()
            q.append(i)
            t = chargeTimes[q[0]] + (i-l+1) * (h[i] - h[l-1])
            if t > budget:
                if q[0] == l:
                    q.popleft()
                l += 1
                continue
            ans = max(ans, i-l+1)
        return ans