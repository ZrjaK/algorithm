# 题目：2217.找到指定长度的回文数
# 难度：MEDIUM
# 最后提交：2022-03-27 17:05:49 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def kthPalindrome(self, queries: List[int], intLength: int) -> List[int]:
        left = (intLength+1) // 2
        ans = []
        mi = 10**(left-1)
        ma = 10**left - 1
        for i in queries:
            if mi + i - 1 > ma:
                ans.append(-1)
                continue
            t = str(mi + i - 1)
            if intLength % 2 == 0:
                ans.append(int(t + t[::-1]))
            else:
                ans.append(int(t + t[:-1][::-1]))
        return ans
        
        