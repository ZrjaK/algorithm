# 题目：剑指 Offer 44.数字序列中某一位的数字
# 难度：MEDIUM
# 最后提交：2022-10-03 18:30:34 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def findNthDigit(self, n: int) -> int:
        if n < 10: return n
        l, cnt, i = 0, 9, 1
        while l+cnt*i < n:
            l += cnt*i
            cnt *= 10
            i += 1
        num = 10**(i-1) + (n-l-1)//i
        index = (n-l-1) % i
        return int(str(num)[index])