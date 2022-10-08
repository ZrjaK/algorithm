# 题目：2357.使数组中所有元素都等于零
# 难度：EASY
# 最后提交：2022-07-31 10:33:22 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        t = []
        for i in nums:
            if i != 0:
                t.append(i)
        if not t:
            return 0
        h = []
        ans = 0
        while t:
            m = min(t)
            for i in t:
                if i != m:
                    h.append(i-m)
            t = h
            h = []
            ans += 1
        return ans