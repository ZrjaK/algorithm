# 题目：1647.字符频次唯一的最小删除次数
# 难度：MEDIUM
# 最后提交：2022-08-31 17:19:41 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def minDeletions(self, s: str) -> int:
        h = sorted(list(Counter(s).values()), reverse=True)
        ans = 0
        for i in range(1, len(h)):
            if h[i] >= h[i-1]:
                if h[i-1]:
                    ans += h[i] - h[i-1] + 1
                    h[i] = h[i-1] - 1
                else:
                    ans += h[i]
                    h[i] = 0
        return ans