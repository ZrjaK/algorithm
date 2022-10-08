# 题目：1036.逃离大迷宫
# 难度：HARD
# 最后提交：2022-09-21 14:57:29 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
        n = len(blocked)
        def check(source, target):
            v = set([(i, j) for i, j in blocked])
            q = deque([(source[0], source[1])])
            while q:
                x, y = q.popleft()
                if (x, y) in v:
                    continue
                v.add((x, y))
                if len(v)-n > n * (n-1) // 2:
                    return True
                if x == target[0] and y == target[1]:
                    return True
                for nx, ny in [[x-1, y], [x+1, y], [x, y+1], [x, y-1]]:
                    if 0<=nx<10**6 and 0<=ny<10**6:
                        q.append((nx, ny))
            return False
        return check(source, target) and check(target, source)