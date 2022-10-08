# 题目：2096.从二叉树一个节点到另一个节点每一步的方向
# 难度：MEDIUM
# 最后提交：2022-08-20 16:22:25 +0800 CST
# 语言：python3
# 作者：ZrjaK

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        fa = {}   # 父节点哈希表
        s = None   # 起点节点
        t = None   # 终点节点

        # 深度优先搜索维护哈希表与起点终点
        def dfs(curr: TreeNode) -> None:
            nonlocal s, t
            if curr.val == startValue:
                s = curr
            if curr.val == destValue:
                t = curr
            if curr.left:
                fa[curr.left] = curr
                dfs(curr.left)
            if curr.right:
                fa[curr.right] = curr
                dfs(curr.right)
        
        dfs(root)

        # 求出根节点到对应节点的路径字符串
        def path(curr: TreeNode) -> List[str]:
            res = []
            while curr != root:
                par = fa[curr]
                if curr == par.left:
                    res.append('L')
                else:
                    res.append('R')
                curr = par
            return res[::-1]
        
        path1 = path(s)
        path2 = path(t)
        # 计算最长公共前缀并删去对应部分，同时将 path_1 逐字符修改为 'U'
        l1, l2 = len(path1), len(path2)
        i = 0
        while i < min(l1, l2):
            if path1[i] == path2[i]:
                i += 1
            else:
                break
        finalpath = 'U' * (l1 - i) + ''.join(path2[i:])   # 最短路径对应字符串 
        return finalpath