# 题目：1640.能否连接形成数组
# 难度：EASY
# 最后提交：2022-09-22 10:07:30 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        h = {v[0]: i for i, v in enumerate(pieces)}
        i = 0
        while i < len(arr):
            if arr[i] not in h:
                return False
            p = pieces[h[arr[i]]]
            if arr[i:i+len(p)] != p:
                return False
            i += len(p)
        return True