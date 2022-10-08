# 题目：344.反转字符串
# 难度：EASY
# 最后提交：2021-10-21 18:10:42 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1