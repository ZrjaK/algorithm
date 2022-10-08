# 题目：2131.连接两字母单词得到的最长回文串
# 难度：MEDIUM
# 最后提交：2022-09-09 17:27:02 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        d = defaultdict(int)
        ans = 0
        for i in words:
            if d[i[1], i[0]]:
                d[i[1], i[0]] -= 1
                ans += 4
            else:
                d[i[0], i[1]] += 1
        for i in range(97, 97+26):
            if d[chr(i), chr(i)]:
                ans += 2
                break
        return ans