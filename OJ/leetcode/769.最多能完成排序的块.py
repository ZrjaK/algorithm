# 题目：769.最多能完成排序的块
# 难度：MEDIUM
# 最后提交：2022-10-13 00:02:27 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        def p(k):
            for i in range(k+1, len(arr)):
                if sorted(arr[k:i]) == list(range(k, i)):
                    return 1 + p(i)
            return 1
        return p(0)