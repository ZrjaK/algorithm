# 题目：2289.使数组按非递减顺序排列
# 难度：MEDIUM
# 最后提交：2022-10-20 12:54:22 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def totalSteps(self, nums: List[int]) -> int:
        ans, st = 0, []
        for num in nums:
            max_t = 0
            while st and st[-1][0] <= num:
                max_t = max(max_t, st.pop()[1])
            max_t = max_t + 1 if st else 0
            ans = max(ans, max_t)
            st.append((num, max_t))
        return ans