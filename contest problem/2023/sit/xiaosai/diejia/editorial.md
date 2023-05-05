简单版本：模拟，时间复杂度 $O(nq)$ 。

困难版本：

使用矩阵来表示每次运算。

技能 $1$ ： 

$$a = k_1 \times a + b$$ 

$$\Downarrow $$

$$
\begin{bmatrix} 
a & b
\end{bmatrix}
\begin{bmatrix}
 k_1 & 0 \\
 1 & 1
\end{bmatrix} = 
\begin{bmatrix}
k_1 \times a + b & b
\end{bmatrix}
$$

技能 $2$ ： 

$$b = a + k_2 \times b$$

$$\Downarrow $$

$$
\begin{bmatrix} 
a & b
\end{bmatrix}
\begin{bmatrix}
 1 & 1 \\
 0 & k_2
\end{bmatrix} = 
\begin{bmatrix}
a & a + k_2 \times b
\end{bmatrix}
$$

在样例一中：$s = 001$，对应的式子是：

$$
\begin{bmatrix} 
1 & 2
\end{bmatrix}
\begin{bmatrix}
 3 & 0 \\
 1 & 1
\end{bmatrix}
\begin{bmatrix}
 3 & 0 \\
 1 & 1
\end{bmatrix}
\begin{bmatrix}
 1 & 1 \\
 0 & 4
\end{bmatrix} = 
\begin{bmatrix}
17 & 25
\end{bmatrix}
$$

由于矩阵运算具有结合律，可以先计算后面三个矩阵相乘结果，最后再左乘 $
\begin{bmatrix} 
a & b
\end{bmatrix}
$ 。

使用线段树来维护每个位置的矩阵，每次询问相当于单点修改，区间查询。

时间复杂度 $O(2^3(n+q)\log n)$ 。

