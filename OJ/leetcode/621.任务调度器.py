# 题目：621.任务调度器
# 难度：MEDIUM
# 最后提交：2022-04-14 19:29:17 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        d = [i for i in Counter(tasks).values()]
        c = d.count(max(d))
        return max((max(d)-1)*(n+1)+c, len(tasks))