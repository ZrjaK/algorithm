// 题目：583.两个字符串的删除操作
// 难度：MEDIUM
// 最后提交：2022-03-21 16:10:23 +0800 CST
// 语言：golang
// 作者：ZrjaK

func minDistance(word1 string, word2 string) int {
    dp := make([][]int, len(word1)+1)
    for i := range dp{
        dp[i] = make([]int, len(word2)+1)
        dp[i][0] = i
    }
    for i := range dp[0] {
        dp[0][i] = i
    }
    for i := 1; i <= len(word1); i++ {
        for j := 1; j <= len(word2); j++ {
            if word1[i-1] == word2[j-1] {
                dp[i][j] = dp[i-1][j-1]
            } else {
                dp[i][j] = Min(dp[i-1][j] + 1, dp[i][j-1] + 1)
            }
        }
    }
    return dp[len(word1)][len(word2)]
}

func Min(arg ...int) int {
	if arg == nil {
		return 0
	}
	r := arg[0]
	for _, v := range arg {
		if v < r {
			r = v
		}
	}
	return r
}