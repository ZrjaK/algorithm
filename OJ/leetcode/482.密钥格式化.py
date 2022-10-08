# 题目：482.密钥格式化
# 难度：EASY
# 最后提交：2021-10-22 13:01:12 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.replace("-", "")[::-1]
        new_s = ""
        for i in range(0, len(s), k):
            new_s += s[i:i+k] + "-"
        new_s = new_s[::-1]
        return new_s[1:].upper()
        