# 题目：2389.和有限的最长子序列
# 难度：EASY
# 最后提交：2022-08-28 10:33:38 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        ans = []
        h = list(accumulate(nums))
        for s in queries:
            t = 0
            for j in range(len(nums)):
                if h[j] <= s:
                    t = j+1
                else:
                    break
            ans.append(t)
        return ans