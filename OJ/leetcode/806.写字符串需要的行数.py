# 题目：806.写字符串需要的行数
# 难度：EASY
# 最后提交：2021-10-24 13:20:41 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        row = 0
        col = 0
        for i in s:
            col += widths[ord(i)-ord("a")]
            if col > 100:
                row += 1
                col = 0
                col += widths[ord(i)-ord("a")]
        return [row+1,col]