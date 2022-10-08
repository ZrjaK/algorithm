// 题目：41.缺失的第一个正数
// 难度：HARD
// 最后提交：2022-03-21 16:49:37 +0800 CST
// 语言：golang
// 作者：ZrjaK

func firstMissingPositive(nums []int) int {
    for i := range nums {
        t := nums[i]
        for t > 0 && t <= len(nums) {
            if t == i+1 || nums[t-1] == t {
                break
            }
            t, nums[t-1] = nums[t-1], t
        }
        nums[i] = t
    }
    for i := range nums {
        if i+1 != nums[i] {
            return i+1
        }
    }
    return len(nums) + 1
}