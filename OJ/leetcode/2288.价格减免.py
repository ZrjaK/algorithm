# 题目：2288.价格减免
# 难度：MEDIUM
# 最后提交：2022-05-29 11:08:12 +0800 CST
# 语言：python3
# 作者：ZrjaK

import re
class Solution:
    def discountPrices(self, sentence: str, discount: int) -> str:
        l = sentence.split(" ")
        for i in range(len(l)):
            if l[i][0] != "$" or l[i].count("$") != 1:
                continue
            try:
                t = int(l[i][1:]) * (100-discount) / 100
                l[i] = "$" + "%.2f"%(t)
            except:
                continue
        return " ".join(l)