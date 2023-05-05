数据范围较大，需要预处理 $10^6$ 内每个数的因子数。

计算每个数会作为哪些数的因子。

枚举 $i=1,2,\dotsb,10^6, j = 1,2,3,\dotsb,k(i * k \le 10^6)$，则 $i$ 是 $i * j$ 的一个因子 。

则总循环次数 $ F = n + \frac{n}{2} + \frac{n}{3} + \dotsb + \frac{n}{n-1} + \frac{n}{n}$ 。

根据调和级数公式 $\sum_{i=1}^{n}\frac{1}{i}=\ln (n+1) + \gamma$ ，所以 $F \approx n \ln n$ 。

最后对 $f(i)$ 做前缀和即可。

时间复杂度为 $O(n\log n + T)$ 。