# 题目：2502.设计内存分配器
# 难度：MEDIUM
# 最后提交：2022-12-11 13:51:48 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Allocator:

    def __init__(self, n: int):
        self.a = [0] * n
        self.d = defaultdict(int)


    def allocate(self, size: int, mID: int) -> int:
        c = 0
        a = self.a
        d = self.d
        for i in range(len(a)):
            if not a[i]:
                c += 1
            else:
                c = 0
            if c == size:
                j = i
                while c:
                    a[j] = 1
                    d[j] = mID
                    j -= 1
                    c -= 1
                return j + 1
        return -1


    def free(self, mID: int) -> int:
        ans = 0
        a = self.a
        d = self.d
        for i in range(len(a)):
            if d[i] == mID:
                a[i] = 0
                ans += 1
                d[i] = -1
        return ans




# Your Allocator object will be instantiated and called as such:
# obj = Allocator(n)
# param_1 = obj.allocate(size,mID)
# param_2 = obj.free(mID)