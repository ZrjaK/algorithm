# 题目：520.检测大写字母
# 难度：EASY
# 最后提交：2021-10-22 15:18:02 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word.upper() == word:
            return True
        if word[1:] == word[1:].lower():
            return True
        return False