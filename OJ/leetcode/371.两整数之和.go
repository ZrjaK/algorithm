// 题目：371.两整数之和
// 难度：MEDIUM
// 最后提交：2022-03-21 03:27:54 +0800 CST
// 语言：golang
// 作者：ZrjaK

func getSum(a int, b int) int {
    yihuo, yu := a ^ b, (a & b) << 1
    for yu != 0 {
        yihuo, yu = yihuo ^ yu, (yihuo & yu) << 1
    }
    return yihuo
}