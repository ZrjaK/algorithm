# 题目：855.考场就座
# 难度：MEDIUM
# 最后提交：2022-12-30 01:02:37 +0800 CST
# 语言：python3
# 作者：ZrjaK

class ExamRoom:

    def __init__(self, n: int):
        self.s = []
        self.n = n

    def seat(self) -> int:
        stu = 0
        s = self.s
        if s:
            d = s[0]
            for i in range(1, len(s)):
                t = s[i]-s[i-1]>>1
                if t > d:
                    d, stu = t, s[i]+s[i-1]>>1
            t = self.n-1-s[-1]
            if t > d:
                stu = self.n-1
        insort(s, stu)
        return stu

    def leave(self, p: int) -> None:
        self.s.remove(p)


# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(n)
# param_1 = obj.seat()
# obj.leave(p)