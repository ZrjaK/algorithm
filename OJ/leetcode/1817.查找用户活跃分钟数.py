# 题目：1817.查找用户活跃分钟数
# 难度：MEDIUM
# 最后提交：2023-01-20 03:44:01 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        ans = [0] * k
        d = defaultdict(set)
        for i, t in logs:
            d[i].add(t)
        for i in d.values():
            ans[len(i)-1] += 1
        return ans