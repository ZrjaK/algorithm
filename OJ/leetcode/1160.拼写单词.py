# 题目：1160.拼写单词
# 难度：EASY
# 最后提交：2021-11-06 22:50:40 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        ans = 0
        for w in words:
            for i in w:
                if w.count(i) > chars.count(i):
                    break
            else:
                ans+=len(w)
        return ans