# 题目：2135.统计追加字母可以获得的单词数
# 难度：MEDIUM
# 最后提交：2022-08-27 01:46:58 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:
        d = defaultdict(int)
        for s in startWords:
            t = 0
            for i in s:
                t |= 1<<ord(i)-97
            d[t] += 1
        ans = 0
        for s in targetWords:
            t = 0
            for i in s:
                t |= 1<<ord(i)-97
            for i in range(26):
                if 1<<i & t:
                    if d[t ^ 1<<i]:
                        ans += 1
                        break
        return ans