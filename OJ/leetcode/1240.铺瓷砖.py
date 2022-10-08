# 题目：1240.铺瓷砖
# 难度：HARD
# 最后提交：2022-09-26 15:22:00 +0800 CST
# 语言：python3
# 作者：ZrjaK

from functools import lru_cache

class Solution:
    def tilingRectangle(self, n: int, m: int) -> int:
        @lru_cache(maxsize=None)
        def dfs(x, y):
            #3种base case
            if x == y:
                return 1
            if x == 1:
                return y
            if y == 1:
                return x
            
            # 最多的划分当然是分成1x1的方格，需要x*y个
            result = x * y
            
            # 情况1
            for i in range(1, (x // 2) + 1):
                result = min(result, dfs(i, y) + dfs(x - i, y))
            
            # 情况2
            for k in range(1, (y // 2) + 1):
                result = min(result, dfs(x, k) + dfs(x, y - k))
            
            # 情况3：中间的小方格的上限大小为长宽较小值-1，其他4个部分的长宽按照图3给出的值计算
            for centre_sq_size in range(1, min(x, y)):
                for i in range(1, x - centre_sq_size):
                    for k in range(1, y - centre_sq_size):
                        partition1 = dfs(i + centre_sq_size, k)
                        partition2 = dfs(x - i - centre_sq_size, k + centre_sq_size)
                        partition3 = dfs(i, y - k)
                        partition4 = dfs(x - i, y - k - centre_sq_size)
                        partition5 = 1 # The central square just needs one block
                        #结果为5个部分相加
                        result = min(result, partition1 + partition2 + partition3 + partition4 + partition5)
            
            return result
        
        return dfs(n, m)