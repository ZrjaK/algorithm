# 题目：1418.点菜展示表
# 难度：MEDIUM
# 最后提交：2022-08-30 18:05:32 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        menu = sorted(list(set(i[2] for i in orders)))
        res = [["Table"] + menu]
        m = {v:i  for i, v in enumerate(menu)}
        d = defaultdict(lambda: [0] * len(menu))
        for _, i, j in orders:
            d[i][m[j]] += 1
        for i in sorted(d, key=lambda x:int(x)):
            t = [i] + [str(j) for j in d[i]]
            res.append(t)
        return res