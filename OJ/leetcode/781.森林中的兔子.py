# 题目：781.森林中的兔子
# 难度：MEDIUM
# 最后提交：2022-09-06 21:48:06 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        d = defaultdict(int)
        for i in answers:
            if d[i]:
                d[i] -= 1
            else:
                d[i] = i
        return len(answers) + sum(d.values())