# 题目：剑指 Offer II 043.往完全二叉树添加节点
# 难度：MEDIUM
# 最后提交：2022-10-06 21:21:55 +0800 CST
# 语言：python3
# 作者：ZrjaK

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class CBTInserter:

    def __init__(self, root: TreeNode):
        self.root = root
        self.candidate = deque()

        q = deque([root])
        while q:
            node = q.popleft()
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
            if not (node.left and node.right):
                self.candidate.append(node)

    def insert(self, val: int) -> int:
        candidate_ = self.candidate

        child = TreeNode(val)
        node = candidate_[0]
        ret = node.val
        
        if not node.left:
            node.left = child
        else:
            node.right = child
            candidate_.popleft()
        
        candidate_.append(child)
        return ret

    def get_root(self) -> TreeNode:
        return self.root


# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(val)
# param_2 = obj.get_root()