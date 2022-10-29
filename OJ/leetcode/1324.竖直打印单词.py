# 题目：1324.竖直打印单词
# 难度：MEDIUM
# 最后提交：2022-10-25 19:30:57 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def printVertically(self, s: str) -> List[str]:
        words = s.split()
        maxlen = max(len(word) for word in words)
        ans = list()
        for i in range(maxlen):
            concat = "".join([word[i] if i < len(word) else " " for word in words])
            ans.append(concat.rstrip())
        return ans