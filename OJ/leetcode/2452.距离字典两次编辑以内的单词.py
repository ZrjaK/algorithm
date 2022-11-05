# 题目：2452.距离字典两次编辑以内的单词
# 难度：MEDIUM
# 最后提交：2022-10-29 22:39:41 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        def calc(s1, s2):
            c = 0
            for i, j in zip(s1, s2):
                if i != j:
                    c += 1
            return c
        ans = []
        for i in queries:
            for j in dictionary:
                if calc(i, j) <= 2:
                    ans.append(i)
                    break
        return ans