# 题目：345.反转字符串中的元音字母
# 难度：EASY
# 最后提交：2021-10-21 18:22:16 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] not in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
                left += 1
                continue
            if s[right] not in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
                right -= 1
                continue
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        return "".join(s)
