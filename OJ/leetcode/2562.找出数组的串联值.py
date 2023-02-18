# 题目：2562.找出数组的串联值
# 难度：EASY
# 最后提交：2023-02-12 10:31:36 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        q = deque(nums)
        ans = 0
        while len(q) > 1:
            t1 = q.popleft()
            t2 = q.pop()
            ans += int(str(t1) + str(t2))
        if q:
            ans += q[0]
        return ans