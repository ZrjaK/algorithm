# 题目：30.串联所有单词的子串
# 难度：HARD
# 最后提交：2022-09-30 10:36:21 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        c = Counter(words)
        n = len(s)
        m = len(words)
        l = len(words[0])
        ans = []
        for i in range(n):
            t = s[i:i+m*l]
            f = Counter()
            for j in range(0, len(t), l):
                f[t[j:j+l]] += 1
            if f == c:
                ans.append(i)
        return ans