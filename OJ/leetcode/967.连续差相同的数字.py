# 题目：967.连续差相同的数字
# 难度：MEDIUM
# 最后提交：2022-08-04 02:14:19 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        res = []
        q = deque([(1, i) for i in range(10)])
        while q:
            i, t = q.popleft()
            if i == n:
                if t >= 10**(n-1):
                    res.append(t)
                continue
            c = t // 10**(i-1)
            if c-k >= 0:
                q.append((i+1, (c-k)*10**i+t))
            if c+k <= 9:
                q.append((i+1, (c+k)*10**i+t))
        return list(set(res))
