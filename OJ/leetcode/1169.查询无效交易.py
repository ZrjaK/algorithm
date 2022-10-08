# 题目：1169.查询无效交易
# 难度：MEDIUM
# 最后提交：2022-08-30 15:09:06 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        trans = [x.split(',') for x in transactions]
        res = []
        for i in range(len(trans)):
            name, time, money, city = trans[i]
            time = int(time)
            if int(money) > 1000:
                res.append(transactions[i])
                continue
            for j in range(len(trans)):
                if i == j:
                    continue
                name1, time1, money1, city1 = trans[j]
                if name1 == name and city1 != city and abs(int(time1) - time) <= 60:
                    res.append(transactions[i])
                    break
        return res