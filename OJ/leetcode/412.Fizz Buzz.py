# 题目：412.Fizz Buzz
# 难度：EASY
# 最后提交：2021-10-21 20:15:22 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        l = []
        for i in range(1, n+1):
            if i % 15 == 0:
                l.append("FizzBuzz")
                continue
            if i % 3 == 0:
                l.append("Fizz")
                continue
            if i % 5 == 0:
                l.append("Buzz")
                continue
            l.append(str(i))
        return l
            