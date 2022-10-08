# 题目：433.最小基因变化
# 难度：MEDIUM
# 最后提交：2022-04-08 01:52:54 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        bank = set(bank)
        if end not in bank:
            return -1
        queue = deque([[start, 0]])
        c = {'A': 'TCG', 'T': 'ACG', 'C': 'ATG', 'G': 'ATC'}
        while queue:
            node, step = queue.popleft()
            if node == end:
                return step
            for i, v in enumerate(node):
                for j in c[v]:
                    new = node[:i] + j + node[i+1:]
                    if new in bank:
                        queue.append([new, step+1])
                        bank.remove(new)
        return -1