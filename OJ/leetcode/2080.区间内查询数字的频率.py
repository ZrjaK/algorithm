# 题目：2080.区间内查询数字的频率
# 难度：MEDIUM
# 最后提交：2022-05-18 23:04:51 +0800 CST
# 语言：python3
# 作者：ZrjaK

class RangeFreqQuery:

    def __init__(self, arr: List[int]):
        self.d = defaultdict(list)
        for i, v in enumerate(arr):
            self.d[v].append(i)

    def query(self, left: int, right: int, value: int) -> int:
        return bisect_right(self.d[value], right) - bisect_left(self.d[value], left) 


# Your RangeFreqQuery object will be instantiated and called as such:
# obj = RangeFreqQuery(arr)
# param_1 = obj.query(left,right,value)