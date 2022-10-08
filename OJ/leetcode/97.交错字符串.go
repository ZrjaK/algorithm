// 题目：97.交错字符串
// 难度：MEDIUM
// 最后提交：2022-03-24 01:39:15 +0800 CST
// 语言：golang
// 作者：ZrjaK

func isInterleave(s1 string, s2 string, s3 string) bool {
    if len(s1) + len(s2) != len(s3) {
        return false
    }
    dp := make([][]bool, len(s1)+1)
    for i := range dp {
        dp[i] = make([]bool, len(s2)+1)
        dp[i][0] = s1[:i] == s3[:i]
    }
    for i := 0; i <= len(s2); i++ {
        dp[0][i] = s2[:i] == s3[:i]
    }
    for i := 1; i <= len(s1); i++ {
        for j := 1; j <= len(s2); j++ {
            if i+j-1 < len(s3) {
                dp[i][j] = (s1[i-1]==s3[i+j-1] && dp[i-1][j]) || 
                        (s2[j-1]==s3[i+j-1] && dp[i][j-1])
            }
        }
    }
    return dp[len(s1)][len(s2)]
}