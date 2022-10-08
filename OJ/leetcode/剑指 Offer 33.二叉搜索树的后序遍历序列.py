# 题目：剑指 Offer 33.二叉搜索树的后序遍历序列
# 难度：MEDIUM
# 最后提交：2022-10-02 22:48:42 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def verifyPostorder(self, postorder: List[int]) -> bool:
        if not postorder:
            return True
        root = postorder[-1]
        left = [i for i in postorder if i < root]
        right = [i for i in postorder if i > root]
        if postorder[:len(left)] == left and postorder[-len(right)-1:-1] == right:
            return self.verifyPostorder(left) and self.verifyPostorder(right)
        return False