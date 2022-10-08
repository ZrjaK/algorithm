# 题目：2048.下一个更大的数值平衡数
# 难度：MEDIUM
# 最后提交：2022-09-14 13:51:30 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        while 1:
            n += 1
            c = Counter(str(n))
            for i in c:
                if int(i) != c[i]:
                    break
            else:
                return n