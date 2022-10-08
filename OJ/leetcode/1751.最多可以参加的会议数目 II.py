# 题目：1751.最多可以参加的会议数目 II
# 难度：HARD
# 最后提交：2022-09-16 08:46:55 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        n = len(events)
        events.sort(key=lambda x: x[1])
        end = [i[1] for i in events]
        dp = [[0] * (k+1) for _ in range(n)]
        m = [[0] * (k+1) for _ in range(n)]
        for i in range(n):
            for j in range(1, min(k, i+1)+1):
                t = bisect_right(end, events[i][0]-1)
                if t == 0:
                    dp[i][1] = events[i][2]
                else:
                    dp[i][j] = m[t-1][j-1] + events[i][2]
                m[i][j] = max(m[i-1][j], dp[i][j])
        return max(max(i) for i in dp)
