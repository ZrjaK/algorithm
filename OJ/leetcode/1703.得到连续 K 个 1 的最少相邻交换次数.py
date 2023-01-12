# 题目：1703.得到连续 K 个 1 的最少相邻交换次数
# 难度：HARD
# 最后提交：2022-12-18 04:15:50 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def minMoves(self, nums: List[int], k: int) -> int:
        n = len(nums)
        def calc(k1, k2):
            s = 0
            q = deque()
            h1, h2 = [1e99] * n, [1e99] * n
            for i in range(n):
                if len(q) > k1:
                    s -= q.popleft()
                if len(q) == k1 and nums[i]:
                    h1[i] = (i-k1 + i-1) * k1 // 2 - s
                if nums[i]:
                    q.append(i)
                    s += i
            s = 0
            q.clear()
            for i in range(n-1, -1, -1):
                if len(q) > k2:
                    s -= q.popleft()
                if len(q) == k2 and nums[i]:
                    h2[i] = s - (i+k2 + i+1) * k2 // 2
                if nums[i]:
                    q.append(i)
                    s += i
            return min(i+j for i, j in zip(h1, h2))
        l, r = (k-1)//2, (k-1)//2 + ((k-1)&1)
        return min(calc(l, r), calc(r, l))