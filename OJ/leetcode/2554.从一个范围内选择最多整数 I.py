# 题目：2554.从一个范围内选择最多整数 I
# 难度：MEDIUM
# 最后提交：2023-02-04 22:32:00 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        ans = 0
        s = 0
        ban = set(banned)
        for i in range(1, n+1):
            if i in ban:
                continue
            if s + i <= maxSum:
                ans += 1
                s += i
        return ans
                