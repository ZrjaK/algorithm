# 题目：2559.统计范围内的元音字符串数
# 难度：MEDIUM
# 最后提交：2023-02-05 10:34:57 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        n = len(words)
        h = [0] * (n+1)
        for i in range(n):
            h[i] = h[i-1]
            if words[i][0] in "aeiou" and words[i][-1] in "aeiou":
                h[i] += 1
        ans = []
        for l, r in queries:
            ans.append(h[r]-h[l-1])
        return ans