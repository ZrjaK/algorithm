# 题目：792.匹配子序列的单词数
# 难度：MEDIUM
# 最后提交：2022-11-17 15:20:16 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        h = [list() for _ in range(26)]
        for i, a in enumerate(s):
            h[ord(a)-97].append(i)
        ans = 0
        for w in words:
            f = 1
            t = -1
            for i in w:
                j = bisect_right(h[ord(i)-97], t)
                if j == len(h[ord(i)-97]):
                    f = 0
                    break
                t = h[ord(i)-97][j]
            ans += f
        return ans