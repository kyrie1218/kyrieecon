# Latex常用数学元素
> [!Note]
> 本文介绍了latex常用的数学元素，包括如下几部分：
>  - 希腊字母
>  - 分段函数

## 分段函数
使用`\begin{align}....\end{align}`模块：
```latex
\begin{align}
f(x) = 
\begin{cases}
2x & x>0 \\
x^{2} & x \leq 0
\end{cases}
\end{align}
```