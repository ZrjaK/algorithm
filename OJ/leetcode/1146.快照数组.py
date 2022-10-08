# 题目：1146.快照数组
# 难度：MEDIUM
# 最后提交：2022-04-05 04:24:06 +0800 CST
# 语言：python3
# 作者：ZrjaK

class SnapshotArray:

    def __init__(self, length: int):
        self.d = defaultdict(list)
        self.c = 0

    def set(self, index: int, val: int) -> None:
        self.d[index].append((self.c, val))

    def snap(self) -> int:
        self.c += 1
        return self.c - 1

    def get(self, index: int, snap_id: int) -> int:
        l, r = 0, len(self.d[index])
        while l < r:
            m = l+r >> 1
            if self.d[index][m][0] <= snap_id:
                l = m+1
            else:
                r = m
        return self.d[index][l-1][1] if l - 1 >= 0 else 0


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)