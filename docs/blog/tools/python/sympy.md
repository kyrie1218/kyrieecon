## 1. 简介
SymPy是Python中的一个优秀的符号和数值计算库。其官网为[https://www.sympy.org/en/index.html](https://www.sympy.org/en/index.html).本文使用1.9版本。示例代码存放在`/code/sympy_example.py`中。

## 2. 一个简单的例子

>[!Attention] 求解如下的非线性方程组：
> $$
> 2x+y^{1/2}=5 \\
> x^2+xy = 5x
> $$

```python
# 导入sympy库
import sympy as sym
# 定义符号
x, y = sym.symbols('x, y')
# 定义方程组
eq1 = sym.Eq(2*x+y**(1/2),5)
eq2 = sym.Eq(x**2+x*y,5*x)
# 求解方程组的精确解
solutions = sym.solve([eq1,eq2],[x,y],dict=True)
# 打印对应的解
print(solutions)
```
对应的输出如下：

![](https://raw.githubusercontent.com/kyrie1218/picgo/main/img/Screenshot%20from%202022-06-09%2020-27-52.png ':size=85%')

即该方程组有两组解：
$$
(x_{1} = 0, y_{1} = 25) \\
(x_{2} = 1.57460947032089, y_{2} = 3.42539052967911)
$$

## 3. 专题
### 3.1 方程组求解

