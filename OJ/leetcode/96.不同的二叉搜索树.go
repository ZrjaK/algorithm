// 题目：96.不同的二叉搜索树
// 难度：MEDIUM
// 最后提交：2022-03-20 19:46:50 +0800 CST
// 语言：golang
// 作者：ZrjaK

func numTrees(n int) int {
    dp := make([]int, n+1)
    dp[0] = 1
    dp[1] = 1
    for i := 2; i <= n; i++ {
        for j := 0; j < i; j++ {
           dp[i] += dp[j] * dp[i-1-j]    
        }
    }
    return dp[n]
}