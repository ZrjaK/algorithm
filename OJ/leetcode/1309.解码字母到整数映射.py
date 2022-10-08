# 题目：1309.解码字母到整数映射
# 难度：EASY
# 最后提交：2022-04-28 20:28:33 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def freqAlphabets(self, s: str) -> str:
        return re.sub(r'\d\d#|\d', lambda x: chr(int(x.group()[:2]) + 96), s)