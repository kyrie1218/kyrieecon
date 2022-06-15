## 解读python代码：RBC模型

```python
import numpy as np # 导入处理array的包
import mpmath as mp # 导入处理高精度计算的包
from scipy import optimize, stats # 导入数值优化和统计的包

class Model(object):  # 定义一个类名叫Model，默认继承object类
    
    def __init__(self, params, k, **kwargs): # 定义python类的初始化方法，参数包含默认的self; 两个位置参数params, k; 任意关键词参数**kwargs
        """A discrete time version of the classic Solow (1956) model of
        economic growth. 
        Summary of exogenous parameters of the Solow Model:
        
            1. g:     growth rate of technology
            2. n:     population growth rate
            3. delta: rate of capital depreciation
            4. alpha: capital share of output
            5. s:     savings rate
            6. theta: (optional) coefficient of relative risk aversion
            7. beta:  (optional) discount factor 
            8. rho:   (optional) persistence of the technology shock
            9. sigma: (optional) standard deviation of the technology 
                      disturbance
            
        Required attributes: 
        
            1. params: a dictionary of parameter values for the model, 
                       i.e. {'alpha':0.33,...}.
            2. k:      a number representing the initial condition of 
                       the state variable (i.e., capital per effective 
                       worker.
        Optional kwargs: 
            1. 'stochastic': If you wish to simulate a stochastic 
                             version of the Solow model, then you will
                             need set this flag to True.
            2. 'seed':       a seed value for the random number 
                             generator (required if 'stochastic'=True).
         
        """ # 对类的简单描述和参数的解释和传入方法。
```

## 重要术语
- python类的初始化方法


## 代码来源
> [!Attention] [https://github.com/davidrpugh/pyeconomics/blob/master/models/solow/solow.py](https://github.com/davidrpugh/pyeconomics/blob/master/models/solow/solow.py)
>
> 已复制到本地`docs/code/rbc.ipynb`。