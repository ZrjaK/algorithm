# 题目：301.删除无效的括号
# 难度：HARD
# 最后提交：2022-08-02 02:55:56 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def check(t):
            l = r = 0
            for i in t:
                if i == "(":
                    l += 1
                if i == ")":
                    r += 1
                if r > l:
                    return False
            return l == r
        res = []
        q = deque([s])
        visited = set()
        while q:
            t = q.popleft()
            if t in visited:
                continue
            if res and len(t) < len(res[0]):
                continue
            visited.add(t)
            if check(t):
                res.append(t)
            for i in range(len(t)):
                q.append(t[:i] + t[i+1:])
        return res