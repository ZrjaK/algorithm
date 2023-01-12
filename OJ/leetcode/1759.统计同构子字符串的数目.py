# 题目：1759.统计同构子字符串的数目
# 难度：MEDIUM
# 最后提交：2022-12-26 00:38:03 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def countHomogenous(self, s: str) -> int:
        ans = 0
        cnt = 0
        c = '1'
        for i in s:
            if i != c:
                ans += cnt * (cnt + 1) // 2
                cnt = 0
                c = i
            cnt += 1
        ans += cnt * (cnt + 1) // 2
        return ans % int(1e9+7)