// 题目：2206.将数组划分成相等数对
// 难度：EASY
// 最后提交：2022-03-19 22:33:30 +0800 CST
// 语言：golang
// 作者：ZrjaK

func divideArray(nums []int) bool {
    m := map[int]int{}
    for _, n := range nums {
        m[n]++
    }
    for _, n := range m {
        if n % 2 == 1{
            return false
        }
    }
    return true
}