# 题目：927.三等分
# 难度：HARD
# 最后提交：2022-10-06 01:14:26 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def threeEqualParts(self, arr: List[int]) -> List[int]:
        n = len(arr)
        s = sum(arr)
        if s % 3:
            return [-1, -1]
        t = 0
        ans = [-1, -1]
        for i in range(n-1, -1, -1):
            t |= arr[i]<<(n-1-i)
            if t.bit_count() == s // 3:
                ans[1] = i
                break
        f = 0
        for i in range(n):
            f = (f<<1) + arr[i]
            if f == t:
                ans[0] = i
                break
        f = 0
        for i in range(ans[0]+1, ans[1]):
            f = (f<<1) + arr[i]
            if f == t:
                ans[1] = i+1
                break
        else:
            return [-1, -1]
        return ans