# 题目：2512.奖励最顶尖的 K 名学生
# 难度：MEDIUM
# 最后提交：2022-12-24 22:42:22 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def topStudents(self, positive_feedback: List[str], negative_feedback: List[str], report: List[str], student_id: List[int], k: int) -> List[int]:
        n = len(report)
        positive_feedback = set(positive_feedback)
        negative_feedback = set(negative_feedback)
        score = [0] * n
        for i in range(n):
            report[i] = Counter(report[i].split(" "))
            for w in report[i]:
                if w in positive_feedback:
                    score[i] += report[i][w] * 3
                    
                if w in negative_feedback:
                    score[i] -= report[i][w]
        
        h = [[i, j] for i, j in zip(score, student_id)]
        h.sort(key=lambda x:(-x[0], x[1]))
        return [i[1] for i in h[:k]]