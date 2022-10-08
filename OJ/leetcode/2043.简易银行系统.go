// 题目：2043.简易银行系统
// 难度：MEDIUM
// 最后提交：2022-03-18 11:39:28 +0800 CST
// 语言：golang
// 作者：ZrjaK

type Bank struct {
    a map[int]int64
}


func Constructor(balance []int64) Bank {
    b := Bank{a: make(map[int]int64,len(balance)+1)}
    for i := range balance {
        b.a[i+1] = balance[i]
    }
    return b
}


func (this *Bank) Transfer(account1 int, account2 int, money int64) bool {
    if a1, ok := this.a[account1]; ok {
        if _, ok := this.a[account2];ok && a1 >= money {
            this.a[account1] -= money
            this.a[account2] += money
            return true
        }
    }
    return false
}


func (this *Bank) Deposit(account int, money int64) bool {
    if _, ok := this.a[account]; ok {
        this.a[account] += money
        return true
    }
    return false
}


func (this *Bank) Withdraw(account int, money int64) bool {
    if a, ok := this.a[account]; ok && a >= money {
        this.a[account] -= money
        return true
    }
    return false
}


/**
 * Your Bank object will be instantiated and called as such:
 * obj := Constructor(balance);
 * param_1 := obj.Transfer(account1,account2,money);
 * param_2 := obj.Deposit(account,money);
 * param_3 := obj.Withdraw(account,money);
 */