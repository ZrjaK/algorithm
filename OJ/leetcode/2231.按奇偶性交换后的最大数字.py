# 题目：2231.按奇偶性交换后的最大数字
# 难度：EASY
# 最后提交：2022-04-10 10:39:41 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def largestInteger(self, num: int) -> int:
        a, b = [], []
        for i in str(num):
            if int(i)%2==1:
                a.append(i)
            else:
                b.append(i)
        a.sort()
        b.sort()
        ans = ""
        for i in str(num):
            if int(i)%2 == 1:
                ans += a.pop()
            else:
                ans += b.pop()
        return int(ans)