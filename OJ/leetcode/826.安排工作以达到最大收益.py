# 题目：826.安排工作以达到最大收益
# 难度：MEDIUM
# 最后提交：2022-04-21 06:15:25 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        a = [[d,p] for d,p in zip(difficulty, profit)]
        a.sort(key=lambda x:x[1],reverse=True)
        a.sort(key=lambda x:x[0])
        for i in range(1,len(a)):
            a[i][1] = max(a[i][1],a[i-1][1])
        ans = 0
        print(a)
        for w in worker:
            l, r = 0, len(a)-1
            while l < r:
                mid = l+r>>1
                if a[mid][0] < w:
                    l = mid + 1
                else:
                    r = mid
            print(l)
            if a[l][0] > w:
                ans += a[l-1][1] if l != 0 else 0
            else:
                ans += a[l][1]
        return ans