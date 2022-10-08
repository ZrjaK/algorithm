# 题目：752.打开转盘锁
# 难度：MEDIUM
# 最后提交：2022-07-30 01:40:55 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        def plus_one(s: str, i: int) -> str:
            s = list(s)
            s[i] = str((int(s[i]) + 1) % 10)
            return ''.join(s)
        
        def sub_one(s: str, i: int) -> str:
            s = list(s)
            s[i] = str((int(s[i]) + 10 - 1) % 10)
            return ''.join(s)

        us = set(deadends)
        if "0000" in us:
            return -1
        
        q = collections.deque()
        visited = set()
        visited.add("0000")
        q.append("0000")
        step = 0
        while q:
            for _ in range(len(q)):
                x = q.popleft()
                if x == target:
                    return step
                for i in range(4):
                    for y in [plus_one(x, i), sub_one(x, i)]:
                        if y not in visited and y not in us:
                            visited.add(y)
                            q.append(y)
            step += 1
        return -1