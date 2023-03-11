# 题目：1599.经营摩天轮的最大利润
# 难度：MEDIUM
# 最后提交：2023-03-05 11:12:31 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        ans = -1
        maxProfit = totalProfit = operations = customersCount = 0
        for c in customers:
            operations += 1
            customersCount += c
            curCustomers = min(customersCount, 4)
            customersCount -= curCustomers
            totalProfit += boardingCost * curCustomers - runningCost
            if totalProfit > maxProfit:
                maxProfit = totalProfit
                ans = operations

        if customersCount == 0:
            return ans

        profitEachTime = boardingCost * 4 - runningCost
        if profitEachTime <= 0:
            return ans

        if customersCount > 0:
            fullTimes = customersCount // 4
            totalProfit += profitEachTime * fullTimes
            operations += fullTimes
            if totalProfit > maxProfit:
                maxProfit = totalProfit
                ans = operations

            remainingCustomers = customersCount % 4
            remainingProfit = boardingCost * remainingCustomers - runningCost
            totalProfit += remainingProfit
            if totalProfit > maxProfit:
                operations += 1
                ans += 1
        return ans
