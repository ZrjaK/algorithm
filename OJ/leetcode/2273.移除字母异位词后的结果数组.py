# 题目：2273.移除字母异位词后的结果数组
# 难度：EASY
# 最后提交：2022-05-15 10:33:16 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        n = len(words)
        res = [words[0]]
        for i in range(1,n):
            if "".join(sorted(list(res[-1]))) == "".join(sorted(list(words[i]))):
                continue
            res.append(words[i])
        return res