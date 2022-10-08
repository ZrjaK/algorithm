# 题目：1299.将每个元素替换为右侧最大元素
# 难度：EASY
# 最后提交：2022-04-03 16:02:24 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        m = arr[-1]
        for i in range(2, len(arr)+1):
            arr[-i], m = m, max(m, arr[-i])
        arr[-1] = -1
        return arr