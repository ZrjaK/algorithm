# 题目：1296.划分数组为连续数字的集合
# 难度：MEDIUM
# 最后提交：2022-04-03 15:48:43 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        if not len(nums) % k == 0:
            return False
        c = Counter(nums)
        for i in sorted(nums):
            if c[i] == 0:
                continue
            for j in range(k):
                if i+j not in c or c[i+j] == 0:
                    return False
                c[i+j] -= 1
        return True