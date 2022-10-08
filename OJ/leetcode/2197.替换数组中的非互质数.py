# 题目：2197.替换数组中的非互质数
# 难度：HARD
# 最后提交：2022-09-16 10:21:49 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        stack = []
        for i in nums:
            stack.append(i)
            while len(stack) > 1:
                x, y = stack[-1], stack[-2]
                if gcd(x, y) == 1:
                    break
                stack.pop()
                stack.pop()
                stack.append(lcm(x, y))
        return stack