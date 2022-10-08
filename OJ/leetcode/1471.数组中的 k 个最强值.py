# 题目：1471.数组中的 k 个最强值
# 难度：MEDIUM
# 最后提交：2022-06-10 15:39:17 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        arr.sort()
        m = arr[(len(arr)-1)//2]
        arr.sort(key=lambda x:(abs(x-m), x), reverse=True)
        return arr[:k]