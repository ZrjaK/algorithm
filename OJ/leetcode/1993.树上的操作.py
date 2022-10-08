# 题目：1993.树上的操作
# 难度：MEDIUM
# 最后提交：2022-08-12 14:55:11 +0800 CST
# 语言：python3
# 作者：ZrjaK

from collections import defaultdict
from typing import List


class LockingTree:

    def __init__(self, parent: List[int]):
        self.parents = defaultdict(int)
        self.sons = defaultdict(list)
        self.locks = defaultdict(int)
        self.prepare(parent)

    def prepare(self, parent: List[int]) -> None:
        for s, p in enumerate(parent):
            self.parents[s] = p
            self.sons[p].append(s)

    def lock(self, num: int, user: int) -> bool:
        if num in self.locks:
            return False
        self.locks[num] = user
        return True

    def unlock(self, num: int, user: int) -> bool:
        if num in self.locks and self.locks[num] == user:
            self.locks.pop(num)
            return True
        return False

    def upgrade(self, num: int, user: int) -> bool:
        if num in self.locks:
            return False
        if self.has_locked_parents(num):
            return False
        locked_sons = self.has_locked_sons(num)
        if not locked_sons:
            return False
        else:
            for son in locked_sons:
                self.locks.pop(son)
        self.locks[num] = user
        return True

    def has_locked_sons(self, num: int) -> List[int]:
        locked_sons = []
        for son in self.sons[num]:
            if son in self.locks:
                locked_sons.append(son)
            locked_sons.extend(self.has_locked_sons(son))
        return locked_sons

    def has_locked_parents(self, num: int) -> bool:
        while True:
            if num == -1:
                return False
            par = self.parents[num]
            if par in self.locks:
                return True
            num = par

# Your LockingTree object will be instantiated and called as such:
# obj = LockingTree(parent)
# param_1 = obj.lock(num,user)
# param_2 = obj.unlock(num,user)
# param_3 = obj.upgrade(num,user)