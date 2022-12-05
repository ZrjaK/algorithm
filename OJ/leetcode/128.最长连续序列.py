# 题目：128.最长连续序列
# 难度：MEDIUM
# 最后提交：2022-11-27 16:50:11 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        v = set()
        parent = {}
        count = {}
        def find(index: int) -> int:
            if parent[index] != index:
                parent[index] = find(parent[index])
            return parent[index]
        
        def union(index1: int, index2: int):
            count[find(index2)] += count[find(index1)] 
            parent[find(index1)] = find(index2)
        
        for i in nums:
            if i in v:
                continue
            v.add(i)
            parent[i] = i
            count[i] = 1
            if i-1 in v:
                union(i, i-1)
            if i+1 in v:
                union(i, i+1)
        return max(count.values())