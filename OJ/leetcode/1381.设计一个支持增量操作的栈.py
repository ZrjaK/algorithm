# 题目：1381.设计一个支持增量操作的栈
# 难度：MEDIUM
# 最后提交：2022-09-04 20:36:26 +0800 CST
# 语言：python3
# 作者：ZrjaK

class CustomStack:

    def __init__(self, maxSize: int):
        self.stk = [0] * maxSize
        self.add = [0] * maxSize
        self.top = -1

    def push(self, x: int) -> None:
        if self.top != len(self.stk) - 1:
            self.top += 1
            self.stk[self.top] = x

    def pop(self) -> int:
        if self.top == -1:
            return -1
        ret = self.stk[self.top] + self.add[self.top]
        if self.top != 0:
            self.add[self.top - 1] += self.add[self.top]
        self.add[self.top] = 0
        self.top -= 1
        return ret

    def increment(self, k: int, val: int) -> None:
        lim = min(k - 1, self.top)
        if lim >= 0:
            self.add[lim] += val



# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)