# 题目：1455.检查单词是否为句中其他单词的前缀
# 难度：EASY
# 最后提交：2022-08-21 17:53:05 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        l = sentence.split(" ")
        ans = -2
        for i in range(len(l)):
            if l[i][:len(searchWord)] == searchWord:
                ans = i
                break
        return ans + 1