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