# 题目：1376.通知所有员工所需的时间
# 难度：MEDIUM
# 最后提交：2022-08-09 02:10:34 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        d = defaultdict(list)
        for i in range(n):
            if i == headID:
                continue
            d[manager[i]].append(i)
        q = deque([(0, headID)])
        ans = 0
        while q:
            s, t = q.popleft()
            ans = max(ans, s)
            for nxt in d[t]:
                q.append((s+informTime[t], nxt))
        return ans
