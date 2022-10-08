# 题目：2341.数组能形成多少数对
# 难度：EASY
# 最后提交：2022-07-17 10:33:17 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        c = Counter(nums)
        ans = [0] * 2
        for i in c.keys():
            ans[0] += c[i] // 2
            ans[1] += c[i] % 2
        return ans