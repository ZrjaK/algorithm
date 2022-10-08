# 题目：895.最大频率栈
# 难度：HARD
# 最后提交：2022-09-15 21:50:33 +0800 CST
# 语言：python3
# 作者：ZrjaK

class FreqStack:

    def __init__(self):
        self.c = defaultdict(int)
        self.d = defaultdict(list)
        self.m = 0

    def push(self, val: int) -> None:
        self.c[val] += 1
        if self.c[val] > self.m:
            self.m = self.c[val]
        self.d[self.c[val]].append(val)

    def pop(self) -> int:
        v = self.d[self.m].pop()
        self.c[v] -= 1
        while not self.d[self.m] and self.m:
            self.m -= 1
        return v


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()