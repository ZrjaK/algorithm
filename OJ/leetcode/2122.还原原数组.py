# 题目：2122.还原原数组
# 难度：HARD
# 最后提交：2022-09-21 14:32:44 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def recoverArray(self, nums: List[int]) -> List[int]:
        n = len(nums) // 2
        nums.sort()
        for j in nums[1:]:
            k = j-nums[0]>>1
            if not k:
                continue
            d = defaultdict(int)
            ans = []
            for i in nums:
                if d[i-2*k]:
                    ans.append(i-k)
                    d[i-2*k] -= 1
                else:
                    d[i] += 1
            if all(i == 0 for i in d.values()):
                return ans