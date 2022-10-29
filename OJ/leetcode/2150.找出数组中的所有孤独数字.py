# 题目：2150.找出数组中的所有孤独数字
# 难度：MEDIUM
# 最后提交：2022-10-24 18:34:54 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        c = Counter(nums)
        ans = []
        for i in nums:
            if c[i] == 1 and c[i-1] == 0 and c[i+1] == 0:
                ans.append(i)
        return ans