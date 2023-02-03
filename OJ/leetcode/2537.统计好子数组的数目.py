# 题目：2537.统计好子数组的数目
# 难度：MEDIUM
# 最后提交：2023-01-15 10:53:47 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        n = len(nums)
        d = defaultdict(int)
        l = 0
        c = 0
        ans = 0
        for i in range(n):
            c += d[nums[i]]
            d[nums[i]] += 1
            
            if c >= k:
                while c >= k:
                    d[nums[l]] -= 1
                    c -= d[nums[l]]
                    l += 1
                l -= 1
                c += d[nums[l]]
                d[nums[l]] += 1
                if c >= k:
                    ans += l + 1
        return ans