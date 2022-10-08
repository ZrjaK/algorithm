# 题目：1652.拆炸弹
# 难度：EASY
# 最后提交：2022-09-24 11:55:58 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        code += code
        if k >= 0:
            return [sum(code[i:i+k]) for i in range(1, n+1)]
        code = code[::-1]
        return [sum(code[i:i-k]) for i in range(1, n+1)][::-1]