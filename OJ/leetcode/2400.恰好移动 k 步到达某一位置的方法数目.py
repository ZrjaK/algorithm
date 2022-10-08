# 题目：2400.恰好移动 k 步到达某一位置的方法数目
# 难度：MEDIUM
# 最后提交：2022-09-04 10:34:14 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        @cache
        def p(i, rest):
            if rest == 0:
                if i == endPos:
                    return 1
                else:
                    return 0
            
            return p(i-1, rest-1) + p(i+1, rest-1)
        return p(startPos, k) % int(1e9+7)