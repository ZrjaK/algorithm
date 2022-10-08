# 题目：17.电话号码的字母组合
# 难度：MEDIUM
# 最后提交：2022-09-14 10:46:41 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        d = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        def p(i):
            if i == len(digits):
                return [""]
            res = []
            for j in d[digits[i]]:
                for x in p(i+1):
                    res.append(j+x)
            return res
        return p(0)