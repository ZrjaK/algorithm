# 题目：2183.统计可以被 K 整除的下标对数目
# 难度：HARD
# 最后提交：2022-09-26 15:44:16 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        c = Counter(gcd(i, k) for i in nums)
        ans = 0
        for i in c:
            for j in c:
                if i * j % k == 0:
                    ans += c[i] * c[j]
        for i in nums:
            if i * i % k == 0:
                ans -= 1
        return ans // 2