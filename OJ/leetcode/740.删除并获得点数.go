// 题目：740.删除并获得点数
// 难度：MEDIUM
// 最后提交：2022-03-16 11:14:08 +0800 CST
// 语言：golang
// 作者：ZrjaK

func deleteAndEarn(nums []int) int {
	trans := make([]int, 10001)
	for _, v := range nums {
		trans[v] += v
	}
	N := len(trans)
	dp := make([]int, N)
	dp[N-1] = trans[N-1]
	for i := N - 2; i >= 0; i-- {
		if i+2 >= N {
			dp[i] = max(trans[i], trans[i+1])
		} else if i+3 >= N {
			dp[i] = max(dp[i+2]+trans[i], trans[i+1])
		} else {
			dp[i] = max(dp[i+2]+trans[i], dp[i+3]+trans[i+1])
		}
	}
	return dp[0]
}

func max(a int, b int) int {
	if a > b {
		return a
	}
	return b
}