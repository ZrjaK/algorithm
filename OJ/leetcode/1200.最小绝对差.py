# 题目：1200.最小绝对差
# 难度：EASY
# 最后提交：2021-11-13 21:41:33 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        l1 = len(arr)
        l2 = len(arr)-1
        minnum = [0]*l2
        for i in range(l2):
            minnum[i] = abs(arr[i+1] - arr[i])
        m = min(minnum)
        res = []
        for i in range(l2):
            if minnum[i] == m:
                res.append([arr[i],arr[i+1]])
        return res