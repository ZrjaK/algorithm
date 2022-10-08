// 题目：2208.将数组和减半的最少操作次数
// 难度：MEDIUM
// 最后提交：2022-03-19 23:49:15 +0800 CST
// 语言：java
// 作者：ZrjaK

class Solution {
    public int halveArray(int[] nums) {
        Queue<Double> queue = new PriorityQueue<>(Collections.reverseOrder());
        double sum = 0;
        for(int i = 0;i < nums.length; i++) {
            double k = nums[i];
            queue.offer(k);
            sum += k;
        }
        double t = sum;
        int count = 0;
        while(t > sum / 2) {
            double tmp = queue.poll() / 2;
            t -= tmp;
            queue.offer(tmp);
            count++;
        }
        return count;
    }
}