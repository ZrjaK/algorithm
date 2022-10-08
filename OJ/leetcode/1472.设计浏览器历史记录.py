# 题目：1472.设计浏览器历史记录
# 难度：MEDIUM
# 最后提交：2022-09-04 23:08:54 +0800 CST
# 语言：python3
# 作者：ZrjaK

class BrowserHistory:

    def __init__(self, homepage: str):
        self.stack = [homepage]
        self.i = 0

    def visit(self, url: str) -> None:
        self.stack = self.stack[:self.i+1]
        self.stack.append(url)
        self.i += 1

    def back(self, steps: int) -> str:
        self.i -= steps
        self.i = max(self.i, 0)
        return self.stack[self.i]

    def forward(self, steps: int) -> str:
        self.i += steps
        self.i = min(self.i, len(self.stack)-1)
        return self.stack[self.i]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)