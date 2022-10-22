# 题目：705.设计哈希集合
# 难度：EASY
# 最后提交：2022-10-21 16:57:52 +0800 CST
# 语言：python3
# 作者：ZrjaK

class MyHashSet:

    def __init__(self):
        self.set = [False] * (10**6+1)

    def add(self, key):
        self.set[key] = True

    def remove(self, key):
        self.set[key] = False

    def contains(self, key):
        return self.set[key]

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)