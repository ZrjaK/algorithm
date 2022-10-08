# 题目：932.漂亮数组
# 难度：MEDIUM
# 最后提交：2022-09-13 12:56:47 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    @cache
    def beautifulArray(self, n: int) -> List[int]:
        if n == 1:
            return [1]
        return [2*i-1 for i in self.beautifulArray((n+1)//2)] + \
                [2*i for i in self.beautifulArray(n//2)]