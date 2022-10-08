# 题目：2402.会议室 III
# 难度：HARD
# 最后提交：2022-09-04 11:12:40 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        room = [0] * n
        res = [0] * n
        meetings.sort(key=lambda x:(x[0], x[1]-x[0]), reverse=True)
        k = 1
        while meetings:
            f = meetings.pop()
            for t in range(n):
                if room[t] <= f[0]:
                    room[t] = max(room[t], f[0]) + f[1]-f[0]
                    res[t] += 1
                    break
            else:  
                t = room.index(min(room))
                room[t] = max(room[t], f[0]) + f[1]-f[0]
                res[t] += 1
        # print(res)
        return res.index(max(res))