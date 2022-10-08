# 题目：2244.完成所有任务需要的最少轮数
# 难度：MEDIUM
# 最后提交：2022-04-17 10:36:41 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        c = Counter(tasks)
        ans = 0
        for i in c.values():
            if i == 1:
                return -1
            ans += i // 3
            if i % 3 != 0:
                ans += 1
        return ans