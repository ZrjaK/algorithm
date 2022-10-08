# 题目：290.单词规律
# 难度：EASY
# 最后提交：2021-10-21 17:32:11 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        if len(s) != len(pattern):
            return False
        for i in range(len(pattern)):
            for j in range(i+1, len(pattern)):
                if pattern[i:i+1] == pattern[j:j+1] and s[i] != s[j]:
                    return False
                if s[i] == s[j] and pattern[i:i+1] != pattern[j:j+1]:
                    return False
        return True