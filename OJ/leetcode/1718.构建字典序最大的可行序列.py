# 题目：1718.构建字典序最大的可行序列
# 难度：MEDIUM
# 最后提交：2022-04-12 11:15:20 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        res = [0 for _ in range(2 * n - 1)]
        visited = [False for _ in range(n + 1)]
        
        def backtrace(i: int) -> bool:
            if i >= 2 * n - 1:
                return True
            if res[i] != 0:
                return backtrace(i + 1)
            for x in range(n, 0, -1):
                if visited[x] == True:
                    continue
                if x == 1:       #1只出现1次，要单独判断
                    visited[1] = True       #借
                    res[i] = 1              #借
                    if backtrace(i + 1) == True:
                        return True
                    res[i] = 0              #回溯==有借有还
                    visited[1] = False      #回溯
                else:
                    if i + x >= 2 * n - 1:
                        continue
                    if res[i] != 0 or res[i + x] != 0:
                        continue
                    res[i] = x              #借
                    res[i + x] = x          #借
                    visited[x] = True       #借
                    if backtrace(i + 1) == True:
                        return True
                    visited[x] = False      #回溯==有借有还
                    res[i + x] = 0          #回溯
                    res[i] = 0              #回溯
            return False
        
        backtrace(0)
        return res