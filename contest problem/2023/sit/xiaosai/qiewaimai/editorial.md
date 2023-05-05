考虑枚举左端点 $l$ ，发现每个端点的贡献为 $a[l,n]$ 与 $a$ 的最长公共前缀。

使用 [Z 函数（扩展 KMP）](https://oi-wiki.org/string/z-func/)即可在线性时间内求解 。

时间复杂度 $O(n)$ 。