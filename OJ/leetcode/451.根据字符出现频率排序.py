# 题目：451.根据字符出现频率排序
# 难度：MEDIUM
# 最后提交：2022-08-27 23:31:11 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def frequencySort(self, s: str) -> str:
        c = Counter(s)
        h = []
        for i in c:
            h.append((c[i], i))
        h.sort(reverse=True)
        ans = ""
        for i, a in h:
            ans += a * i
        return ans