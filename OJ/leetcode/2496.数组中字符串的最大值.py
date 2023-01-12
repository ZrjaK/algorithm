# 题目：2496.数组中字符串的最大值
# 难度：EASY
# 最后提交：2022-12-10 22:30:53 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        ans = 0
        for i in strs:
            try:
                ans = max(ans, int(i))
            except:
                ans = max(ans, len(i))
        return ans