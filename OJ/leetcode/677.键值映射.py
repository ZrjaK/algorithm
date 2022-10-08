# 题目：677.键值映射
# 难度：MEDIUM
# 最后提交：2022-10-08 12:27:54 +0800 CST
# 语言：python3
# 作者：ZrjaK

class MapSum:

    def __init__(self):
        self.d = {}

    def insert(self, key: str, val: int) -> None:
        self.d[key] = val

    def sum(self, prefix: str) -> int:
        return sum(self.d[w] for w in self.d if w.startswith(prefix))

# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)