# Numpy
## 1. 简介
Numpy是处理向量或者矩阵的一个Python第三方库。Anaconda已经包含了numpy库。其操作的基本数据类型为`ndarray`(n维数组)。实例代码在`/code/numpy_example.ipynb`中。

## 2. 一个简单的例子
```python
import numpy as np # 导入numpy库

# 创建一个ndarray
a = np.array([1,2,1])
print(a)

# 操作这个array
a.size # 查看元素个数
a.ndim # 查看维度
```

## 3.专题
### 3.1 创建ndarray
```python
# 1. 零ndarray
b = np.zeros(100)
print(b)

c = np.zeros((2,3),dtype = 'int64')
print(c)
# 2. 单位ndarry
one_a = np.ones((3,2),dtype='int64')
print(one_a)

# 3. 随机ndarry
rand_a = np.random.rand(4,3) # 4行3列的连续均匀分布[0,1)
print(rand_a)

randint_a = np.random.randint([1 3],10,size=(5,3)) # 5行3列的离散均匀分布[1,10)
print(randint_a)



```
### 3.2 代数运算
```python
# 1. array的乘法（星乘/点乘/矩阵乘）
a = np.array([1, 2, 3, 4, 5])
b = np.array([0, 1, 3, 4, 6])
a*b # 两个相同shape的ndarray可以进行星乘(*)，即相同位置的元素求积
# left blank for dot and matrix products


```