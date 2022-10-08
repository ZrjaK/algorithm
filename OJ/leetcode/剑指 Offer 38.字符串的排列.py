# 题目：剑指 Offer 38.字符串的排列
# 难度：MEDIUM
# 最后提交：2022-10-03 11:19:17 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def permutation(self, s: str) -> List[str]:
        return ["".join(i) for i in set(list(permutations(s)))]