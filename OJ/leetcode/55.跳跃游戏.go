// 题目：55.跳跃游戏
// 难度：MEDIUM
// 最后提交：2022-03-16 09:53:11 +0800 CST
// 语言：golang
// 作者：ZrjaK

func canJump(nums []int) bool {
	index := len(nums) - 1
	nums[index] = index
	for i := len(nums) - 2; i >= 0; i-- {
		if i+nums[i] < nums[i+1] {
			nums[i] = nums[i+1]
		} else {
			index = i
			nums[i] = index
		}
	}
	return nums[0] == 0
}