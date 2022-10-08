# 题目：12.整数转罗马数字
# 难度：MEDIUM
# 最后提交：2022-09-30 10:24:14 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def intToRoman(self, num: int) -> str:
        d = {
            1000: "M",
            900:  "CM",
            500:  "D",
            400:  "CD",
            100:  "C",
            90:   "XC",
            50:   "L",
            40:   "XL",
            10:   "X",
            9:    "IX",
            5:    "V",
            4:    "IV",
            1:    "I"}
        ans = ""
        while num:
            for i in sorted(d, reverse=True):
                if i <= num:
                    ans += d[i]
                    num -= i
                    break
        return ans