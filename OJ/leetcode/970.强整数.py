# 题目：970.强整数
# 难度：MEDIUM
# 最后提交：2022-12-11 22:07:22 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        i = 1
        d = defaultdict(int)
        while i < bound:
            j = 1
            while j < bound:
                if i + j <= bound:
                    d[i+j] += 1
                if y == 1:
                    break
                j *= y
            if x == 1:
                break
            i *= x
        return list(d.keys())