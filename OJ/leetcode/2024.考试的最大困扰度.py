# 题目：2024.考试的最大困扰度
# 难度：MEDIUM
# 最后提交：2022-05-18 21:35:56 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def maxConsecutiveAnswers(self, s: str, k: int) -> int:
        n = len(s)
        l, r = 1, n
        ans = 0
        while l <= r:
            mid = l+r>>1
            i, j = 0, mid
            countT = 0
            countF = 0
            for a in range(mid):
                if s[a] == "T":
                    countT += 1
                else:
                    countF += 1
            t = max(countT, countF)
            while j < len(s):
                if s[j] == "T":
                    countT += 1
                else:
                    countF += 1
                j += 1
                if s[i] == "T":
                    countT -= 1
                else:
                    countF -= 1
                i += 1
                t = max(t, max(countT, countF))
            if mid - t > k:
                r = mid - 1
            else:
                ans = l
                l = mid + 1
        return l-1