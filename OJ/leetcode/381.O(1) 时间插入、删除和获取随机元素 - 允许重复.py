# 题目：381.O(1) 时间插入、删除和获取随机元素 - 允许重复
# 难度：HARD
# 最后提交：2022-10-20 16:08:56 +0800 CST
# 语言：python3
# 作者：ZrjaK

class RandomizedCollection:
    def __init__(self):
        from sortedcontainers import SortedList
        self.a = SortedList()
        self.d = {}

    def insert(self, val: int) -> bool:
        res = val not in self.d or not self.d[val]
        if not res:
            self.d[val] += 1
        else:
            self.d[val] = 1
        self.a.add(val)
        return res

    def remove(self, val: int) -> bool:
        if val not in self.d or not self.d[val]:
            return False
        self.d[val] -= 1
        self.a.remove(val)
        return True

    def getRandom(self) -> int:
        return self.a[randint(0, len(self.a)-1)]


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()