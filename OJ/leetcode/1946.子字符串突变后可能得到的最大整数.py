# 题目：1946.子字符串突变后可能得到的最大整数
# 难度：MEDIUM
# 最后提交：2022-09-08 20:27:53 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def maximumNumber(self, num: str, change: List[int]) -> str:
        s = list(num)
        for i in range(len(s)):
            if change[int(s[i])] > int(s[i]):
                for j in range(i, len(s)):
                    if change[int(s[j])] < int(s[j]):
                        break
                    s[j] = str(change[int(s[j])])
                break
        return "".join(s)