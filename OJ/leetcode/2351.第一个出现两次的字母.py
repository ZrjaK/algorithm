# 题目：2351.第一个出现两次的字母
# 难度：EASY
# 最后提交：2022-07-24 10:31:07 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def repeatedCharacter(self, s: str) -> str:
        a = [0] * 26
        for i in s:
            a[ord(i)-97] += 1
            for j in range(26):
                if a[j] == 2:
                    return chr(j+97)