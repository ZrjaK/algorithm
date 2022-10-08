# 题目：1053.交换一次的先前排列
# 难度：MEDIUM
# 最后提交：2022-09-06 23:45:30 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        if sorted(arr) == arr:
            return arr
        n = len(arr)
        for i in range(n-2, -1, -1):
            if arr[i] <= arr[i+1]:
                continue
            h = sorted(arr[i+1:], reverse=True)
            for t in h:
                if t < arr[i]:
                    break
            else:
                continue
            for j in range(i+1, n):
                if arr[j] == t:
                    break
            arr[i], arr[j] = arr[j], arr[i]
            return arr 