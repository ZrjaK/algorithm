# 题目：599.两个列表的最小索引总和
# 难度：EASY
# 最后提交：2021-10-23 10:37:30 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        index1 = {list1[i]: i for i in range(len(list1))}
        index2 = {list2[i]: i for i in range(len(list2))}
        agreements = set(list1) & set(list2)
        sum_index = {r: index1[r]+index2[r] for r in agreements}
        return [r for r in agreements if sum_index[r] == min(sum_index.values())]
                    
