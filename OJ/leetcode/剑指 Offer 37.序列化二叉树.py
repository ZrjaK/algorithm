# 题目：剑指 Offer 37.序列化二叉树
# 难度：HARD
# 最后提交：2022-10-03 11:17:11 +0800 CST
# 语言：python3
# 作者：ZrjaK

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        if not root:
            return "n"

        res = str(root.val)
        res += 'l' + self.serialize(root.left)
        res += 'r' + self.serialize(root.right)
        return res

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if data == "n":
            return None
        i = data.index('l')

        left = 1
        right = 0
        n = len(data)
        for j in range(i+1, n):
            left += int(data[j]=='l')
            right += int(data[j]=='r')
            if left == right:
                break
        root = TreeNode(int(data[:i]))
        root.left = self.deserialize(data[i+1:j])
        root.right = self.deserialize(data[j+1:])
        return root
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))