# 题目：2409.统计共同度过的日子数
# 难度：EASY
# 最后提交：2022-09-17 22:40:47 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        d = {1:31, 2:28, 3:31, 4:30,5:31, 6:30,7:31,8:31,9:30,10:31,11:30,12:31}
        def calc(s):
            s, l = [int(i) for i in s.split("-")]
            a = 0
            for i in range(1, 13):
                if i < s:
                    a += d[i]
                else:
                    a += l
                    break
            return a
        aa, la, ab, lb = calc(arriveAlice), calc(leaveAlice), calc(arriveBob), calc(leaveBob)
        # print(aa, la, ab, lb)
        if la < ab or lb < aa:
            return 0
        return min(la, lb)-max(aa, ab) + 1
        
        