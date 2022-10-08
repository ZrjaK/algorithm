# 题目：2191.将杂乱无章的数字排序
# 难度：MEDIUM
# 最后提交：2022-09-01 16:44:19 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        # 制作翻译表
        tab = str.maketrans("0123456789", "".join(map(str, mapping)))
        # 自定义排序: (num2map,idx)
        return sorted(nums, key=lambda x: int(str(x).translate(tab)))