# 题目：1255.得分最高的单词集合
# 难度：HARD
# 最后提交：2023-02-26 00:07:31 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        C = Counter(letters)
        n = len(words)
        ans = 0
        for mask in range(1<<n):
            c = Counter()
            for i in range(n):
                if mask >> i & 1:
                    c += Counter(words[i])
            if all(c[i] <= C[i] for i in c):
                s = 0
                for i in c:
                    s += c[i] * score[ord(i) - 97]
                ans = max(ans, s)
        return ans