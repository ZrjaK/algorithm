# 题目：1720.解码异或后的数组
# 难度：EASY
# 最后提交：2022-08-26 21:16:20 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        res = [first]
        for i in encoded:
            res.append(res[-1] ^ i)
        return res