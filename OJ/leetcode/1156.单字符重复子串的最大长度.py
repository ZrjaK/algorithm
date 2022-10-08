# 题目：1156.单字符重复子串的最大长度
# 难度：MEDIUM
# 最后提交：2022-05-26 00:09:22 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def maxRepOpt1(self, text: str) -> int:
        ans = 0
        c = Counter(text)
        i = 0
        while i < len(text):
            leng = 0
            while i + leng < len(text) and text[i+leng] == text[i]:
                leng += 1
            j = i + leng + 1
            w = 0
            while j + w < len(text) and text[j+w] == text[i]:
                w += 1
            ans = max(ans, min(w+leng+1, c[text[i]]))
            i += leng
        return ans