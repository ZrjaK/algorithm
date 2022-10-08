// 题目：198.打家劫舍
// 难度：MEDIUM
// 最后提交：2022-03-16 10:54:14 +0800 CST
// 语言：golang
// 作者：ZrjaK

func rob(nums []int) int {
	N := len(nums)
	dp := make([]int, N)
	dp[N-1] = nums[N-1]
	for i := N - 2; i >= 0; i-- {
		if i+2 >= N {
			dp[i] = max(nums[i], nums[i+1])
		} else if i+3 >= N {
			dp[i] = max(dp[i+2]+nums[i], nums[i+1])
		} else {
			dp[i] = max(dp[i+2]+nums[i], dp[i+3]+nums[i+1])
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