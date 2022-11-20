# 题目：2465.不同的平均值数目
# 难度：EASY
# 最后提交：2022-11-13 11:01:31 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        nums.sort()
        q = deque(nums)
        ans = set()
        while q:
            ans.add((q.popleft()+q.pop())/2)
        return len(ans)