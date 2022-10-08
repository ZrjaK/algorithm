# 题目：1356.根据数字二进制下 1 的数目排序
# 难度：EASY
# 最后提交：2022-08-26 21:12:04 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        return sorted(arr, key=lambda x: (x.bit_count(), x))