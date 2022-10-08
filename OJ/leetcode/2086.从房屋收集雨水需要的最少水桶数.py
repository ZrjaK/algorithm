# 题目：2086.从房屋收集雨水需要的最少水桶数
# 难度：MEDIUM
# 最后提交：2022-07-23 02:21:05 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def minimumBuckets(self, street: str) -> int:
        pos = -2
        ans = 0
        for i, ch in enumerate(street):
            if ch == "H":
                if pos == i-1:
                    continue
                elif i+1 < len(street) and street[i+1] == ".":
                    pos = i+1
                    ans += 1
                elif i > 0 and street[i-1] == ".":
                    ans += 1
                else:
                    return -1
        return ans