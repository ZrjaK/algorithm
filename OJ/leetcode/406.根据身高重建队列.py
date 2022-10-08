# 题目：406.根据身高重建队列
# 难度：MEDIUM
# 最后提交：2022-08-30 01:46:27 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        res = []
        for p in sorted(people, key = lambda x: (-x[0], x[1])):
            if len(res) <= p[1]:
                res.append(p)
            elif len(res) > p[1]:
                res.insert(p[1], p)
        return res