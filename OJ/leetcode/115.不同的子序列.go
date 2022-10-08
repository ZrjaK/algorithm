// 题目：115.不同的子序列
// 难度：HARD
// 最后提交：2022-03-24 02:55:59 +0800 CST
// 语言：golang
// 作者：ZrjaK

func numDistinct(s string, t string) int {
    dp := make([][]int, len(s)+1)
    for i := range dp {
        dp[i] = make([]int, len(t)+1)
        dp[i][0] = 1
    }
    for i := 1; i <= len(s); i++ {
        for j := 1; j <= len(t); j++ {
            if j > i {
                continue
            }
            if s[i-1] == t[j-1] {
                dp[i][j] = dp[i-1][j] + dp[i-1][j-1]
                continue
            }
            dp[i][j] = dp[i-1][j]
        }
    }
    return dp[len(s)][len(t)]
}