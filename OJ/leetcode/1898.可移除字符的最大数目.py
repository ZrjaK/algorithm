# 题目：1898.可移除字符的最大数目
# 难度：MEDIUM
# 最后提交：2022-05-16 13:20:02 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        def check(mid):
            se = set(removable[:mid])
            j = 0
            for i in range(len(s)):
                if i in se:
                    continue
                if s[i] == p[j]:
                    j += 1
                if j == len(p):
                    return True
            return False
        l, r = 0, len(removable)
        while l <= r:
            mid = l+r>>1
            if check(mid):
                l = mid + 1
            else:
                r = mid - 1
        return r
