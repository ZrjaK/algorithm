# 题目：2365.任务调度器 II
# 难度：MEDIUM
# 最后提交：2022-08-06 23:09:52 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        n = len(tasks)
        d = {}
        res = 0
        for i in tasks:
            if i in d:
                if res - d[i] <= space:
                    res += space - (res - d[i])
            else:
                d[i] = res
            res += 1
            d[i] = res
        return res
            