// 题目：15.三数之和
// 难度：MEDIUM
// 最后提交：2022-03-08 22:16:06 +0800 CST
// 语言：golang
// 作者：ZrjaK

func threeSum(nums []int) [][]int {
    sort.Ints(nums)
	res:=[][]int{}
	
	for i:=0;i<len(nums)-2;i++{
		n1:=nums[i]
		if n1>0{
			break
		}
		if i>0&&n1==nums[i-1]{
			continue
		}
		l,r:=i+1,len(nums)-1
		for l<r{
			n2,n3:=nums[l],nums[r]
			if n1+n2+n3==0{
				res=append(res,[]int{n1,n2,n3})
				for l<r&&nums[l]==n2{
					l++
				}
				for l<r&&nums[r]==n3{
					r--
				}
			}else if n1+n2+n3<0{
				l++
			}else {
				r--
			}
		}
	}
	return res
}