# 题目：2432.处理用时最长的那个任务的员工
# 难度：EASY
# 最后提交：2022-10-09 10:37:14 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        t = -1
        ans = -1
        for i in range(len(logs)):
            id = logs[i][0]
            time = logs[i][1] - logs[i-1][1] if i else logs[i][1]
            if time > t:
                ans = id
                t = time
            elif time == t:
                ans = min(ans, id)
        return ans