# 题目：524.通过删除字母匹配到字典里最长单词
# 难度：MEDIUM
# 最后提交：2022-06-03 09:24:40 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        def check(st):
            i = j = 0
            while j < len(st):
                if not i < len(s):
                    return False
                if s[i] == st[j]:
                    i += 1
                    j += 1
                else:
                    i += 1
            return True
        ans = ""
        for i in dictionary:
            if len(i) < len(ans) or not check(i):
                continue
            if len(i) == len(ans) and i > ans:
                continue
            ans = i
        return ans