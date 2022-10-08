# 题目：2327.知道秘密的人数
# 难度：MEDIUM
# 最后提交：2022-07-03 11:26:28 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        q = deque()
        q.append(1)
        for _ in range(1, n):
            # print(q)
            while len(q) >= forget:
                q.popleft()
            s = 0
            for i in range(len(q)-delay+1):
                s += q[i]
            q.append(s)
        s = 0
        for i in range(len(q)):
            s += q[i]
        return s % int(1e9 + 7)