// 题目：11.盛最多水的容器
// 难度：MEDIUM
// 最后提交：2022-03-19 20:33:29 +0800 CST
// 语言：golang
// 作者：ZrjaK

func maxArea(height []int) int {
    m := 0
    left := 0
    right := len(height) - 1
    for left < right {
        m = max(m, (right - left) * min(height[left], height[right]))
        if height[left] < height[right] {
            left++
        } else {
            right--
        }
    }
    return m
}

func max(a int, b int) int {
    if a > b {
        return a
    }
    return b
}

func min(a int, b int) int {
    if a < b {
        return a
    }
    return b
}