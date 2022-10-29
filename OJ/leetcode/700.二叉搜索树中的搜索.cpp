// 题目：700.二叉搜索树中的搜索
// 难度：EASY
// 最后提交：2022-10-24 21:47:56 +0800 CST
// 语言：cpp
// 作者：ZrjaK

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    TreeNode* ans;
    TreeNode* searchBST(TreeNode* root, int val) {
        ans = NULL;
        p(root, val);
        return ans;
    }
    void p(TreeNode* node, int val) {
        if (node == NULL) return;
        if (node->val == val) ans = node;
        p(node->left, val), p(node->right, val);
        return;
    }
};