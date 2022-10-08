// 题目：930.和相同的二元子数组
// 难度：MEDIUM
// 最后提交：2022-05-21 11:38:46 +0800 CST
// 语言：golang
// 作者：ZrjaK

func numSubarraysWithSum(nums []int, goal int) (ans int) {
    left1, left2 := 0, 0
    sum1, sum2 := 0, 0
    for right, num := range nums {
        sum1 += num
        for left1 <= right && sum1 > goal {
            sum1 -= nums[left1]
            left1++
        }
        sum2 += num
        for left2 <= right && sum2 >= goal {
            sum2 -= nums[left2]
            left2++
        }
        ans += left2 - left1
    }
    return
}