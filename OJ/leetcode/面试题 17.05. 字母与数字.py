# 题目：面试题 17.05. 字母与数字
# 难度：MEDIUM
# 最后提交：2023-03-11 00:22:41 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def findLongestSubarray(self, array: List[str]) -> List[str]:
        n = len(array)
        h = [0] * n
        for i in range(n):
            if array[i].isdigit():
                h[i] = -1
            else:
                h[i] = 1
        h = list(accumulate(h)) + [0]
        d = defaultdict(list)
        for i in range(n):
            d[h[i]].append(i)
        ans = -1
        ansc = -1
        for i in range(n):
            if h[i-1] in d:
                t = d[h[i-1]][-1]
                if ansc < t - i + 1:
                    ansc = t - i + 1
                    ans = i
        return array[ans:ans + ansc]