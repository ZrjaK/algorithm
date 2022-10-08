# 题目：2177.找到和为给定整数的三个连续整数
# 难度：MEDIUM
# 最后提交：2022-04-11 18:13:36 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        if num % 3 == 0:
            n2 = num // 3
            n1, n3 = n2-1, n2+1
            return [n1,n2,n3]
        return []