# 题目：1963.使字符串平衡的最小交换次数
# 难度：MEDIUM
# 最后提交：2022-06-21 12:50:31 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def minSwaps(self, s: str) -> int:
        ans = 0
        for i in s:
            if i == "]":
                if ans > 0:
                    ans -= 1
            else:
                ans += 1
        return ans // 2 + ans % 2