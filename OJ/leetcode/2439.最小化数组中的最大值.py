# 题目：2439.最小化数组中的最大值
# 难度：MEDIUM
# 最后提交：2022-10-15 23:18:03 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        n = len(nums)
        nums += [0]
        for _ in range(10):
            s = 0
            l = 0
            for r in range(n):
                s += nums[r]
                if s <= nums[r+1] * (r-l+1):
                    continue
                # print(nums, l, r, s)
                for j in range(l, r+1):
                    nums[j] = s // (r-l+1)
                t = s % (r-l+1)
                for j in range(r, l-1, -1):
                    if not t:
                        break
                    nums[j] += 1
                    t -= 1
                # print(nums, l, r, s)
                s = 0
                l = r+1
        return max(nums)