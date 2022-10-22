# 题目：782.变为棋盘
# 难度：HARD
# 最后提交：2022-10-17 15:08:12 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def movesToChessboard(self, board: List[List[int]]) -> int:
        n = len(board)
        # 将行列转为二进制数：交换行列不会影响位运算的异或运算与与运算
        row = []
        for i in range(n):
            row.append(sum(board[i][j]<<j for j in range(n)))

        col = []
        for j in range(n):
            col.append(sum(board[i][j]<<i for i in range(n)))

        def check(lst):
            cnt = Counter(lst)
            x, y = min(cnt), max(cnt)
            # 不满足条件：只有两个数
            if len(cnt) != 2:
                return -1
            # 不满足条件：位运算不是互补
            if x & y or x ^ y != (1 << n) - 1:
                return -1
            # 不满足条件：奇偶个数
            if n % 2 == 0:
                if cnt[x] != cnt[y]:
                    return -1
            else:
                if abs(cnt[x] - cnt[y]) != 1:
                    return -1
            # 列举可能的顺序组合：计算需要操作的次数
            lst1 = []
            lst2 = []
            for k in range(n):
                if k % 2:
                    lst1.append(x)
                    lst2.append(y)
                else:
                    lst1.append(y)
                    lst2.append(x)
            # 贪心比较不同位置的个数：由于两个数一定是成对出现所以除以2即为操作次数
            if Counter(lst1) == cnt:
                cost1 = sum(int(lst[k] != lst1[k]) for k in range(n)) // 2
            else:
                cost1 = 1e99
            if Counter(lst2) == cnt:
                cost2 = sum(int(lst[k] != lst2[k]) for k in range(n)) // 2
            else:
                cost2 = 1e99
            return min(cost1, cost2)

        row_cost = check(row)
        col_cost = check(col)
        if row_cost == -1 or col_cost == -1:
            return -1
        return row_cost + col_cost