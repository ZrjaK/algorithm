# 题目：125.验证回文串
# 难度：EASY
# 最后提交：2021-10-20 22:32:19 +0800 CST
# 语言：python3
# 作者：ZrjaK

import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub("\W", "", s)
        s = re.sub("_", "", s)
        return s.lower() == s[::-1].lower()