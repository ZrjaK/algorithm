# 题目：1286.字母组合迭代器
# 难度：MEDIUM
# 最后提交：2022-09-14 13:23:35 +0800 CST
# 语言：python3
# 作者：ZrjaK

class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        n = len(characters)
        v = set()
        for i in range(1<<n):
            if i.bit_count() != combinationLength:
                continue
            t = ""
            for j in range(n):
                if i>>j&1:
                    t += characters[j]
            v.add(t)
        self.h = sorted(list(v))
        self.p = bisect_right(self.h, characters)-1
    def next(self) -> str:
        res = self.h[self.p]
        self.p += 1
        return res
    def hasNext(self) -> bool:
        return self.p < len(self.h)


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()