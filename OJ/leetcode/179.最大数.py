# 题目：179.最大数
# 难度：MEDIUM
# 最后提交：2022-08-27 17:52:36 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = sorted(map(str, nums), key=cmp_to_key(lambda x, y: int(y+x)-int(x+y)))
        return "0" if nums[0]=="0" else "".join(nums)