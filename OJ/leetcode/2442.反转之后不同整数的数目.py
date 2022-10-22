# 题目：2442.反转之后不同整数的数目
# 难度：MEDIUM
# 最后提交：2022-10-16 10:33:38 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        v = set(str(i) for i in nums)
        for i in nums:
            v.add(str(int(str(i)[::-1])))
        return len(v)
        