# 题目：2342.数位和相等数对的最大和
# 难度：MEDIUM
# 最后提交：2022-07-17 10:37:37 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        d = defaultdict(list)
        for i in nums:
            t = 0
            c = i
            while c:
                t += c % 10
                c //= 10
            d[t].append(i)
        for i in d.keys():
            d[i].sort()
        ans = -1
        for i in d.keys():
            if len(d[i]) >= 2:
                ans = max(ans, d[i][-2]+d[i][-1]) 
        return ans