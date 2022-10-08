# 题目：1585.检查字符串是否可以通过排序子字符串得到另一个字符串
# 难度：HARD
# 最后提交：2022-09-28 15:22:10 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def isTransformable(self, s: str, t: str) -> bool:
        n = len(s)
        pos = {i: collections.deque() for i in range(10)}
        for i, digit in enumerate(s):
            pos[int(digit)].append(i)
        
        for i, digit in enumerate(t):
            d = int(digit)
            if not pos[d]:
                return False
            if any(pos[j] and pos[j][0] < pos[d][0] for j in range(d)):
                return False
            pos[d].popleft()
        
        return True