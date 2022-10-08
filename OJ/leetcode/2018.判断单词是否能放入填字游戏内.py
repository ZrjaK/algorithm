# 题目：2018.判断单词是否能放入填字游戏内
# 难度：MEDIUM
# 最后提交：2022-09-13 09:26:02 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def placeWordInCrossword(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        h = []
        for i in range(m):
            s = "".join(board[i])
            s = s.split("#")
            for j in s:
                if len(j) == len(word):
                    h.append(j)
        for j in range(n):
            s = "".join(board[i][j] for i in range(m))
            s = s.split("#")
            for j in s:
                if len(j) == len(word):
                    h.append(j)
        def check(s):
            p1 = 0
            for i in range(len(word)):
                if s[p1] == word[i] or s[p1] == " ":
                    p1 += 1
                else:
                    return False
            return True
        return any(check(i) or check(i[::-1]) for i in h)