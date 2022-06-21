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
### 4.1. 获取人均有效产出
在ramsey离散时间模型中，当期人均有效产出如下：
$$
y_{t} = k_{t}^{\alpha}
$$
其中，$k_{t}$是时期$t$的人均有效产出，即$k_{t} \equiv K_{t}/(A_{t}N_{t})$。
因此，可将其定义为方法`get_output`如下：
```python
def get_output(self,k):
    """获得人均有效产出。

    输入：
        k: 当前人均有效资本;

    返回：
        y: 当前人均有效产出
    """
    # 获取参数资本收入份额参数alpha
    alpha = self.alpha

    y = k**alpha
    return y

```

### 4.2. 获取人均有效投资
在Ramsey模型中，当期人均有效投资$i_{t}$等于人均有效产出$y_{t}$减去人均有效消费$c_{t}$：
$$
i_{t} = y_{t}-c_{t}
$$
因此，我们可定义方法`get_investment`如下：
```python
def get_investment(self,k,c):
    """获取人均有效投资

    输入：
        k：人均有效资本
        c: 人均有效消费

    返回：
        i： 人均有效投资

    """
    i = self.get_output(k)-c
    return i

```
### 4.3. 获取实际有效工资率
在Ramsey模型，实际工资率等于有效劳动的边际产出决定：
$$
w_{t} =  \frac{\partial Y_{t}}{\partial (A_{t}N_{t})} = \frac{\partial{(K_{t})^{\alpha}(A_{t}N_{t})^{1-\alpha}}}{\partial (A_{t}N_{t})}  \\
= (1-\alpha)\frac{Y_{t}}{A_{t}N_{t}} = (1-\alpha)y_{t}
$$
因此，可以获得`get_wageRate`方法：
```python
def get_wageRate(self,k):
    """获得有效劳动的工资率

    """
    # 抽取资本收入份额参数alpha
    alpha = self.alpha

    # 获得有效劳动的实际工资率
    w = (1-alpha)*self.get_output(k)
    return w

```
### 4.4. 获取实际利率




