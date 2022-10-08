# 题目：825.适龄的朋友
# 难度：MEDIUM
# 最后提交：2022-04-21 05:37:54 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        ages.sort()
        l = r = ans = 0
        for age in ages:
            if age < 15:
                continue
            while ages[l] <= 0.5*age+7:
                l += 1
            while r+1 < len(ages) and ages[r+1] <= age:
                r += 1
            ans += r-l
        return ans