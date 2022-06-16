## 解读python代码：RBC模型

```python
import numpy as np # 导入处理array的包
import mpmath as mp # 导入处理高精度计算的包
from scipy import optimize, stats # 导入数值优化和统计的包

class Model(object):  # 定义一个类名叫Model，默认继承object类
    
    def __init__(self, params, k, **kwargs): # 定义python类的初始化实例方法，参数包含默认的self; 两个位置参数params, k; 任意关键词参数**kwargs
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
         
        """ # 对实例的简单描述和参数的解释和传入方法。
        # initial value of the state variable
        self.k          = k  #将参数k作为属性k

        # create the dictionary of parameter values
        self.param_dict = params # 将参数params作为属性param_dict

        # dictionary of steady state values        
        self.SS_dict    = {'k_star':self.set_k_star()} # 将set_k_star方法获得的稳态值作为初始稳态参数

        # optional keyword arguments (for stochastic model only!)
        self.stochastic = kwargs.get('stochastic', False) # 将可选参数stochastic默认值为False，对应属性值也默认为False
        self.seed       = kwargs.get('seed', None) # 可选关键词参数seed默认为None，其对应属性值也默认为None
        self.z0         = kwargs.get('z0', 1.0) # 可选关键词参数z0默认为1.0,其对应属性值也默认为1.0

        # if simulating a stochastic model, the seed must be set! 设置stochastic和seed参数的额外条件
        if self.stochastic == True and self.seed == None:
            assert "You forgot to set a seed for the RNG!"  # 如果stochastic属性值为真，但seed属性值为None时，提醒声明（这段好像有点将assert用错了地方，更像是在用print)
        elif self.stochastic == True and self.seed != None:
            # set the seed    # 如果stochastic属性值为真，但seed属性值不是None，则进行np.random.seed以设置随机序列的待重复序数。
            np.random.seed(self.seed)
            # create a disturbance term for the technology shock # 根据以上seed，随机一个均值为0,方差为sigma的正态的随机分布实例对象。注意是对象，不是具体的值
            self.eps = stats.norm(0, self.param_dict['sigma'])
        else:
            pass  # else占位，不做任何操作。
```

## 重要术语

- python类的初始化方法

- kwargs.get方法

- Python中的None值

- Python中的assert语句

- np.random.seed方法

- Python中的pass语句

## 代码来源
> [!Attention] [https://github.com/davidrpugh/pyeconomics/blob/master/models/solow/solow.py](https://github.com/davidrpugh/pyeconomics/blob/master/models/solow/solow.py)
>
> 已复制到本地`docs/code/rbc.ipynb`。