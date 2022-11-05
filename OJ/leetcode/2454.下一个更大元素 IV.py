# 题目：2454.下一个更大元素 IV
# 难度：HARD
# 最后提交：2022-10-29 23:36:32 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def secondGreaterElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        h = [-1] * n
        q = []
        q2 = []
        for i in range(n):
            # print(q, q2)
            while q2 and -q2[-1][0] < nums[i]:
                t = q2.pop()[1]
                h[t] = i
            while q and nums[q[-1]] < nums[i]:
                t = q.pop()
                insort(q2, [-nums[t], t])
            q.append(i)
        # print(h)
        ans = []
        for i in h:
            if i == -1:
                ans.append(-1)
            else:
                ans.append(nums[i])
        return ans