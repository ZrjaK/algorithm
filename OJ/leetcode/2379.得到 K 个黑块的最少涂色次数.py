# 题目：2379.得到 K 个黑块的最少涂色次数
# 难度：EASY
# 最后提交：2023-03-09 09:28:52 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        n = len(blocks)
        ans = n
        for i in range(len(blocks)-k+1):
            ans = min(ans, blocks[i:i+k].count("W"))
        return ans