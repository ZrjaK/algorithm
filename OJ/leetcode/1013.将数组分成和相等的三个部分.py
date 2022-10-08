# 题目：1013.将数组分成和相等的三个部分
# 难度：EASY
# 最后提交：2021-11-03 19:46:38 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        target=sum(arr)/3
        if target-int(target)!=0:
            return False
        counter=0
        tmpsum=0
        for i in arr:
            tmpsum+=i
            if tmpsum==target:
                counter+=1
                tmpsum=0

        return True if counter>=3 else False