# 题目：954.二倍数对数组
# 难度：MEDIUM
# 最后提交：2022-05-17 14:56:30 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        arr.sort()
        c = Counter(arr)
        for i in arr:
            if c[i] and c[i*2]:
                c[i] -= 1
                c[i*2] -= 1
        for i in arr:
            if c[i]:
                return False
        return True