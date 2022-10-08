// 题目：45.跳跃游戏 II
// 难度：MEDIUM
// 最后提交：2022-03-16 11:45:49 +0800 CST
// 语言：golang
// 作者：ZrjaK

func jump(nums []int) int {
	dp := make([]int, len(nums))
    index := 0
    for i:= 1; i < len(nums); i++ {
        for i > index + nums[index] {
            index++
        }
        dp[i] = dp[index] + 1
    }
    return dp[len(nums)-1]
}