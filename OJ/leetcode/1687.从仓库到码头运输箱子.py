# 题目：1687.从仓库到码头运输箱子
# 难度：HARD
# 最后提交：2022-12-05 22:00:32 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def boxDelivering(self, boxes: List[List[int]], portsCount: int, maxBoxes: int, maxWeight: int) -> int:
        n = len(boxes)
        h = [0] + list(accumulate(i[1] for i in boxes))
        cost = [0]
        for (i, _), (j, _) in zip(boxes, boxes[1:]):
            cost.append(cost[-1] + int(i != j))
        cost += [0]
        for i in range(1, n):
            cost[i] = cost[i-1]
            cost[i] += int(boxes[i][0] != boxes[i-1][0])
        dp = [1e99] * (n+1)
        dp[0] = 0
        mn = [1e99] * (n+1)
        q = deque()
        for i in range(n+1):
            while q and (i - q[0] > maxBoxes or h[i] - h[q[0]] > maxWeight):
                q.popleft()
            if q:
                dp[i] = cost[i-1] + mn[q[0]] + 2
            mn[i] = dp[i] - cost[i]
            while q and mn[q[-1]] >= mn[i]:
                q.pop()
            q.append(i)
        return dp[-1]