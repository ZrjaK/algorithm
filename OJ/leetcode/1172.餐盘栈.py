# 题目：1172.餐盘栈
# 难度：HARD
# 最后提交：2022-09-19 15:15:12 +0800 CST
# 语言：python3
# 作者：ZrjaK

class DinnerPlates:

    def __init__(self, capacity: int):
        from sortedcontainers import SortedDict
        self.capacity = capacity
        self.stack = defaultdict(list)
        self.left_not_full = SortedDict()
        self.right_not_nan = SortedDict()

    def push(self, val: int) -> None:
        if not self.left_not_full:
        # 注意defaulteddict访问会创造键
            self.left_not_full[len(self.stack)] = 1
        index = self.left_not_full.peekitem(0)[0]
        self.stack[index].append(val)
        self.right_not_nan[index] = 1
        if len(self.stack[index]) == self.capacity:
            self.left_not_full.popitem(0)
        return

    def pop(self) -> int:
        if not self.right_not_nan:
            return -1
        index = self.right_not_nan.peekitem(-1)[0]
        value = self.stack[index].pop(-1)
        if not self.stack[index]:
            self.right_not_nan.popitem(-1)
        self.left_not_full[index] = 1
        return value


    def popAtStack(self, index: int) -> int:
        # 注意defaulteddict访问会创造键
        if index not in self.stack or not self.stack[index]:
            return -1
        value = self.stack[index].pop(-1)
        if not self.stack[index]:
            del self.right_not_nan[index]
        self.left_not_full[index] = 1
        return value


# Your DinnerPlates object will be instantiated and called as such:
# obj = DinnerPlates(capacity)
# obj.push(val)
# param_2 = obj.pop()
# param_3 = obj.popAtStack(index)