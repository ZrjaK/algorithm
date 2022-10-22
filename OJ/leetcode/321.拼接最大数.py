# 题目：321.拼接最大数
# 难度：HARD
# 最后提交：2022-10-20 15:52:46 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        m, n = len(nums1), len(nums2)
        res = []
        def calc(arr, f):
            q = []
            c = len(arr)-f
            for i in range(len(arr)):
                while q and c and arr[q[-1]] < arr[i]:
                    q.pop()
                    c -= 1
                q.append(i)
            return [arr[i] for i in q][:f]
        def merge(a, b):
            i = j = 0
            ans = []
            while a and b:
                if a > b:
                    ans.append(a[0])
                    a = a[1:]
                else:
                    ans.append(b[0])
                    b = b[1:]
            ans += a + b
            return ans
        for i in range(k+1):
            if i <= m and k-i <= n:
                p1 = calc(nums1, i)
                p2 = calc(nums2, k-i)
                t = merge(p1, p2)
                if t > res:
                    res = t
        return res