# 题目：2306.公司命名
# 难度：HARD
# 最后提交：2022-06-12 12:21:02 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        s = set(ideas)
        cnt = [[0] * 26 for _ in range(26)]
        for i in ideas:
            for a in range(97, 97+26):
                if chr(a) + i[1:] not in s:
                    cnt[ord(i[0])-97][a-97] += 1
        ans = 0
        for i in range(26):
            for j in range(26):
                ans += cnt[i][j] * cnt[j][i]
        return ans