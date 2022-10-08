# 题目：1023.驼峰式匹配
# 难度：MEDIUM
# 最后提交：2022-06-09 15:57:11 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        def check(s):
            i = j = 0
            while i < len(s) and j < len(pattern):
                if s[i] == pattern[j]:
                    i += 1
                    j += 1
                    continue
                if 65 <= ord(s[i]) <= 90:
                    return False
                i += 1
            if j != len(pattern):
                return False
            while i < len(s):
                if 65 <= ord(s[i]) <= 90:
                    return False
                i += 1
            return True

        res = []
        for i in queries:
            res.append(check(i))
        return res