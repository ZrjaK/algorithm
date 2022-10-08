# 题目：剑指 Offer II 060.出现频率最高的 k 个数字
# 难度：MEDIUM
# 最后提交：2022-10-08 11:55:27 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [i[0] for i in Counter(nums).most_common()][:k]