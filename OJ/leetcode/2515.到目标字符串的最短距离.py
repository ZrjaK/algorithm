# 题目：2515.到目标字符串的最短距离
# 难度：EASY
# 最后提交：2022-12-25 17:35:23 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def closetTarget(self, words: List[str], target: str, startIndex: int) -> int:
        n = len(words)
        if target not in words:
            return -1
        h = [i for i in range(n) if target == words[i]]
        ans = 1e99
        for t in h:
            if t > startIndex:
                ans = min(ans, t-startIndex, startIndex+n-t)
            else:
                ans = min(ans, startIndex-t, t+n-startIndex)
        return ans