# 题目：2326.螺旋矩阵 IV
# 难度：MEDIUM
# 最后提交：2022-07-03 11:13:52 +0800 CST
# 语言：python3
# 作者：ZrjaK

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        res = [[-1] * n for _ in range(m)]
        def process(p, i, j):
            # print("###")
            if not p:
                return
            right = n-1-j
            left = j
            up = i
            down = m-1-i
            while p and j <= right:
                res[i][j] = p.val
                p = p.next
                j += 1
            j -= 1
            i += 1
            # print(i, j)
            while p and i <= down:
                res[i][j] = p.val
                p = p.next
                i += 1
            i -= 1
            j -= 1
            # print(i, j)
            while p and j >= left:
                res[i][j] = p.val
                p = p.next
                j -= 1
            j += 1
            i -= 1
            # print(i, j)
            while p and i > up:
                res[i][j] = p.val
                p = p.next
                i -= 1
            i += 1
            # print(i, j)
            process(p, i, j+1)
        process(head, 0, 0)
        return res