# 题目：2261.含最多 K 个可整除元素的子数组
# 难度：MEDIUM
# 最后提交：2022-05-01 10:55:22 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        res = set()
        n = len(nums)
        for i in range(n):
            t = 0
            for j in range(i,n):
                if nums[j] % p == 0:
                    t += 1
                if t > k:
                    break
                res.add(tuple(nums[i:j+1]))
        # print(res)
        return len(res)
                        
        