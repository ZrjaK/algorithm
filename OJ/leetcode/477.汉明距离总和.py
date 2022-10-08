# 题目：477.汉明距离总和
# 难度：MEDIUM
# 最后提交：2022-08-25 17:08:28 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        d = [[0] * 2 for _ in range(32)]
        ans = 0
        for i in nums:
            for j in range(32):
                if i & 1<<j:
                    d[j][1] += 1
                    ans += d[j][0]
                else:
                    d[j][0] += 1
                    ans += d[j][1]
        return ans