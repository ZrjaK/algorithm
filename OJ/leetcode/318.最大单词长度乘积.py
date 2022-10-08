# 题目：318.最大单词长度乘积
# 难度：MEDIUM
# 最后提交：2022-04-19 15:45:14 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        def p(s1, s2):
            s = set(s1)
            for i in s2:
                if i in s:
                    return False
            return True
        words.sort(key=lambda x: len(x),reverse=True)
        print(words)
        ans = 0
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if p(words[i],words[j]):
                    ans = max(ans, len(words[i])*len(words[j]))
        return ans