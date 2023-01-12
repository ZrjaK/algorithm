# 题目：2526.找到数据流中的连续整数
# 难度：MEDIUM
# 最后提交：2023-01-07 22:33:53 +0800 CST
# 语言：python3
# 作者：ZrjaK

class DataStream:

    def __init__(self, value: int, k: int):
        self.v = value
        self.k = k
        self.c = 0


    def consec(self, num: int) -> bool:
        if num == self.v:
            self.c += 1
        else:
            self.c = 0
        return self.c >= self.k


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)