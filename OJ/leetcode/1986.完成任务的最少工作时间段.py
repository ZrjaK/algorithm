# 题目：1986.完成任务的最少工作时间段
# 难度：MEDIUM
# 最后提交：2022-07-22 03:54:20 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def minSessions(self, tasks: List[int], sessionTime: int) -> int:
        n = len(tasks)
        @cache
        def p(v, time):
            if v+1 == 2<<n:
                return 0
            res = 1e99
            for i in range(n):
                if not 1<<i & v:
                    v ^= 1<<i
                    if time < tasks[i]:
                        res = min(res, 1 + p(v, sessionTime-tasks[i]))
                    else:
                        res = min(res, p(v, time-tasks[i]))
                    v ^= 1<<i
            return res
        res = 1 + p(1<<n, sessionTime)
        p.cache_clear()
        return res