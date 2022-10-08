# 题目：2102.序列顺序查询
# 难度：HARD
# 最后提交：2022-09-21 14:06:47 +0800 CST
# 语言：python3
# 作者：ZrjaK

class SORTracker:

    def __init__(self):
        from sortedcontainers import SortedSet
        self.s = SortedSet()
        self.c = 0

    def add(self, name: str, score: int) -> None:
        self.s.add((-score, name))

    def get(self) -> str:
        res = self.s[self.c][1]
        self.c += 1
        return res


# Your SORTracker object will be instantiated and called as such:
# obj = SORTracker()
# obj.add(name,score)
# param_2 = obj.get()