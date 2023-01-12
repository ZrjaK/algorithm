# 题目：面试题 16.16.部分排序
# 难度：MEDIUM
# 最后提交：2023-01-02 15:02:22 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def subSort(self, array: List[int]) -> List[int]:
        n = len(array)
        a = sorted(array)
        ans = []
        for i in range(n):
            if a[i] != array[i]:
                ans.append(i)
                break
        for i in range(n-1, -1, -1):
            if a[i] != array[i]:
                ans.append(i)
                break
        return ans if ans else [-1, -1]