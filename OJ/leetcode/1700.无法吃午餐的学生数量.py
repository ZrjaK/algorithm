# 题目：1700.无法吃午餐的学生数量
# 难度：EASY
# 最后提交：2022-10-19 00:00:32 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        q = deque(students)
        sandwiches = sandwiches[::-1]
        while q:
            t = q.popleft()
            if t == sandwiches[-1]:
                sandwiches.pop()
            else:
                q.append(t)
            if all(i != sandwiches[-1] for i in q):
                return len(q)
        return 0