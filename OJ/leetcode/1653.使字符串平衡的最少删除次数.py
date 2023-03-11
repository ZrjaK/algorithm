# 题目：1653.使字符串平衡的最少删除次数
# 难度：MEDIUM
# 最后提交：2023-03-06 08:17:13 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def minimumDeletions(self, s: str) -> int:
        cb = 0
        ca = s.count("a")
        ans = ca + cb
        for i in s:
            if i == "b":
                cb += 1
            else:
                ca -= 1
            ans = min(ans, ca+cb)
        return ans