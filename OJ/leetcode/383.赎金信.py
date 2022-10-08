# 题目：383.赎金信
# 难度：EASY
# 最后提交：2021-10-21 19:15:47 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine = list(magazine)
        for i in ransomNote:
            if i in magazine:
                magazine.remove(i)
            else:
                return False
        return True