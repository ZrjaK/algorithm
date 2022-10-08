# 题目：848.字母移位
# 难度：MEDIUM
# 最后提交：2022-05-22 00:55:03 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        h = list(accumulate(shifts[::-1]))[::-1]
        ans = ""
        for i, j in zip(s, h):
            ans += chr((ord(i) - 97 + j) % 26 + 97)
        return ans