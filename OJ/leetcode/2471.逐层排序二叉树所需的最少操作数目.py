# 题目：2471.逐层排序二叉树所需的最少操作数目
# 难度：MEDIUM
# 最后提交：2022-11-13 10:45:45 +0800 CST
# 语言：python3
# 作者：ZrjaK

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        def calc(arr):
            new_arr = sorted(arr)
            dict_position = {}
            for i in range(len(new_arr)):
                dict_position[new_arr[i]] = i
            res_closure = 0
            flag = [0 for x in arr]
            for i in range(len(arr)):
                if flag[i] == 0:
                    j = i
                    while flag[j] == 0:
                        flag[j] = 1
                        j = dict_position[arr[j]]
                    res_closure += 1
            return len(arr) - res_closure
        q = deque()
        q.append(root)
        res = []
        while q:
            size = len(q)
            t = []
            for _ in range(size):
                cur = q.popleft()
                if not cur:
                    continue
                t.append(cur.val)
                q.append(cur.left)
                q.append(cur.right)
            if t:
                res.append(t)
        ans = 0
        for lst in res:
            ans += calc(lst)
        return ans