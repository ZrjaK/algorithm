# 题目：380.O(1) 时间插入、删除和获取随机元素
# 难度：MEDIUM
# 最后提交：2022-10-05 21:21:16 +0800 CST
# 语言：python3
# 作者：ZrjaK

class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = defaultdict(list)
        self.a = []

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if self.d[val]:
            return False
        self.d[val].append(len(self.a))
        self.a.append(val)
        return True


    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if not self.d[val]:
            return False
        t = self.d[val][-1]
        self.d[self.a[-1]] = [t]
        self.d[val].pop()
        self.a[t] = self.a[-1]
        self.a.pop()
        return True


    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return self.a[randint(0, len(self.a)-1)]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()