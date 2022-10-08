# 题目：948.令牌放置
# 难度：MEDIUM
# 最后提交：2022-06-08 03:48:12 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        l, r = 0, len(tokens) - 1
        ans = 0
        c = 0
        while l <= r:
            if power >= tokens[l]:
                power -= tokens[l]
                l += 1
                c += 1
                ans = max(ans, c)
            elif ans > 0:
                power += tokens[r]
                r -= 1
                c -= 1
                ans = max(ans, c)
            else:
                break
        return ans