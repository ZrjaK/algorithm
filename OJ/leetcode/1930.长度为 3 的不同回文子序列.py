# 题目：1930.长度为 3 的不同回文子序列
# 难度：MEDIUM
# 最后提交：2022-11-27 12:09:34 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        d = {i: defaultdict(int) for i in range(3)}
        ans = 0
        v = set()
        d[0][""] = 1
        for i in s:
            for j in "abcdefghijklmnopqrstuvwxyz":
                t = i+j
                if t in d[2]:
                    v.add(i+j+i)
            for k in range(1, -1, -1):
                for j in d[k]:
                    d[k+1][j+i] = 1
        
        return len(v)