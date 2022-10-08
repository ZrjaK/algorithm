# 题目：933.最近的请求次数
# 难度：EASY
# 最后提交：2022-05-06 00:31:48 +0800 CST
# 语言：python3
# 作者：ZrjaK

class RecentCounter:

    def __init__(self):
        self.queue = deque()


    def ping(self, t: int) -> int:
        self.queue.append(t)
        while (len(self.queue) != 0) and (self.queue[0] < t - 3000):
            self.queue.popleft()
        return len(self.queue)

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)