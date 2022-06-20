# 解读python代码：Ramsey模型类
## 1. 简介
Ramsey模型是新古典宏观经济学的两个标准模型之一（另一个是Diamond模型）。本文将解读[davidrpugh/pyeconomics](https://github.com/davidrpugh/pyeconomics/blob/master/models/ramsey.py)构造Ramsey模型的python类代码。

## 2. 预备第三方库
该类的构造需要用到四个python库及模块：
- numpy 用于构造序列;
- scipy.optimize 用于非线性方程求解;
- scipy.integrate 用于求数值积分;
- scipy.spatial.distance 用于控制误差水平;
- sympy 用于求解稳定性分析的Jocob矩阵;
- mpmath 用于高精度浮点数运算;
- matplotlib.pyplot 用于绘制相位图.

即首先导入所需模块并简化命名：
```python
import numpy as np
import scipy.optimize as opt
import scipy.integrate as odeint
import scipy.spatial.distance as dist
import sympy as sym
import mpmath as mp
import matplotlib.pyplot as plt
```
## 3. 分析类的基本框架
作为一个关于Ramsey模型的python类，我们需要思考如下问题：
- 该RamseyModel类的对象属性是哪些？
- 该RamseyModel类包含哪些对象方法？

首先回答第一个问题。对象需要哪些属性？一般来说，我们将初始化方法的参数和一次性操作作为对象的属性。直白地说，我们需要思考对象*一旦自创建后就保持不变*且需要*预先计算*的*值*是哪些？那些就是我们需要设定的对象属性。在我们的RamseyModel类中，作者使用的属性分为三类：
- 1. 外生参数，包括人口/技术/偏好等;
- 2. 状态变量初始值，包括人均有效消费和人均有效资本
- 3. 其他选项，如时间维度，是否离散时间，内生变量的初始稳态值，稳定性分析参数等等。

确实！外生参数总是我们分析模型时，一直不变的东西，而且是必须的！而内生变量初始值也是进行转移态分析时一次性使用且必须的值！初始稳态是也是进行稳态比较和福利分析预先计算的值！另外，基于初始稳态值的稳定性分析则是需要预先计算的！（但如果是具有新稳态，则稳定性分析就不能作为属性）

现在回到第二个的问题。对象需要哪些方法？这个问题实际上是在问我们的工作包括哪些流程。在RamseyModel类中，即Ramsey模型的分析包括哪些环节？一般跟随如下环节进行分析：
- 1. 竞争均衡的最优化行为;
- 2. 初始稳态的决定;
- 3. 初始稳态的稳定性分析;
- 3. 内生变量转移态的决定规则;
- 4. 获得转移路径并绘制相位图;
- 5. 反事实的内生变量路径(本文没有);
- 6. 反事实的福利水平计算和比较(本文没有);
- 7. 最优政策分析(本文没有).

## 4. 定义方法










