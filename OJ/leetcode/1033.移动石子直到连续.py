# 题目：1033.移动石子直到连续
# 难度：MEDIUM
# 最后提交：2022-06-09 16:09:09 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
        if b < a:
            a, b = b, a
        if c < b:
            b, c = c, b
        if b < a:
            a, b = b, a
        if c-b == 1 and b-a == 1:
            return [0, c-a-2]
        if c-b <= 2 or b-a <= 2:
            return [1, c-a-2]
        return [2, c-a-2]