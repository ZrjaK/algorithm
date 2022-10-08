// 题目：122.买卖股票的最佳时机 II
// 难度：MEDIUM
// 最后提交：2022-03-24 19:52:09 +0800 CST
// 语言：golang
// 作者：ZrjaK

func maxProfit(prices []int) int {
    res := 0
    for i := range prices {
        if i != 0 && prices[i-1] < prices[i] {
            res += prices[i]
        }
        if i != len(prices)-1 && prices[i] < prices[i+1] {
            res -= prices[i]
        }
    }
    return res
}