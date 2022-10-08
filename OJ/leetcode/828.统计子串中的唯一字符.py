# 题目：828.统计子串中的唯一字符
# 难度：HARD
# 最后提交：2022-09-15 23:03:21 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def uniqueLetterString(self, s: str) -> int:
        d = defaultdict(list)
        for i, a in enumerate(s):
            d[a].append(i)
        ans = 0
        for arr in d.values():
            arr = [-1] + arr + [len(s)]
            for i in range(1, len(arr)-1):
                ans += (arr[i]-arr[i-1]) * (arr[i+1]-arr[i])
        return ans