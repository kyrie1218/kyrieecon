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

    # 方法的定义
    def get_utility(self,C): # 定义获取效用流的方法
        """Representative agent has constant relative risk aversion 
        (CRRA) preferences over consumption per worker, C.
        For \theta \neq 1, CRRA preferences are:
        
        u(C_t) = \frac{C_t^{1 - \theta} - 1}{1 - \theta}
        For \theta = 1, CRRA preferences are equivalent to:
        u(C_t) = ln C_t
        The parameter \theta has a dual role.  It is the coefficient 
        of relative risk aversion (the higher is theta, the more risk 
        averse is the representative agent); and it is also the inverse
        of the intertemporal elasticity of substitution (the higher is 
        theta, the less willing is the representative agent to shift
        consumption back and forth across time).
        
        Inputs: consumption per worker, C.
        Returns: utility from consuming C, u(C).
        
        """
        # extract the params
        theta = self.param_dict['theta']

        if theta != 1:
            return (C**(1-theta)-1)/(1-theta)
        else:
            return np.log(C)

    def get_lifetimeUtility(self,c,A0=1,L0=1,H=1):
                """Computes lifetime utility associated with a consumption 
        stream. Note that the function automatically accounts for 
        growth in technology and population. 
    
        Inputs: 
            1. an array, c representing a consumption stream in per 
               effective worker units.
            2. A0: (default = 1) some value for the initial level of 
               technology.
            3. L0: (default = 1) some value for the initial size of 
               labor force.
            4. H: (default = 1) size of the representative household.
        
        Returns: A list containing...
        
            1. Present discount value, in terms of utility, of the 
               consumption stream.
            2. The path of discounted flow utility (for plotting)
    
        """

        # extract the params
        g = self.param_dict['g'] # 外生增长率
        n = self.param_dict['n'] # 外生人口增长率
        beta = self.param_dict['beta'] # 贴现因子

        # time path
        time  = np.arrange(0,np.size(c),1) # 生成时间路径0,1,2,...,所需要的消费流的存在长度
        # need to inflate consumption per effective worker by technology
        tech_path = A0*(1+g)**time # 生成技术进步的序列

        # need to discount future utility from consumption 
        discount_factor = (L0 / float(H))*(beta*(1+n))**time # 生成贴现率序列

        # compute the path of utility
        utility_path  = discount_factor*self.get_utility(c*tech_path)

        return [np.sum(utility_path),utility_path] #返回终生效用和效用流

    # 设定初始稳态的k(资本-有效劳动比)
    def set_k_star(self):
        """The steady-state level of capital stock per effective 
        worker, k_star, in the Solow model is a function of the 
        exogenous parameters!
    
        """
        # extract params
        s = self.param_dict['s']
        n = self.param_dict['n']
        g = self.param_dict['g']
        alpha = self.param_dict['alpha']
        delta = self.param_dict['delta']

        return (s / ((1+g)*(1+n)-(1-delta)))**(1/(1-alpha))

    # 定义k的转移态(由于外生技术冲击zplus的影响)
    def get_newCapital(self, k, zplus):
        """Function that takes end of period t's capital stock per 
        effective worker, k_t, and and a contemporaneous technology 
        shock, z_{t+1}, and returns the end of period t+1's capital 
        stock per effective worker, kplus.
        k_{t+1} = \frac{1}{(1 + g)(1 + n)z_{t+1}}[(1 - \delta)k_t + sk_t^{\alpha}]
        
        Inputs: 
            1. capital per effective worker, k.
            2. technology shock, z (defaults to 1 in every period if
               self.deterministic == True).
        Returns: next period's value of capital per effective worker,
                 kplus.
    
        """ 
        # extract params 
        n = self.param_dict['n']
        g = self.param_dict['g']
        s = self.param_dict['s']
        alpha = self.param_dict['alpha']
        delta = self.param_dict['delta']

        # next period's capital per effective worker
        kplus = (1/((1+g)*(1+n)*zplus))*((1-delta)*k+s*k**alpha)

        return kplus
    
    # 定义外生冲击的序列
    def get_newTechShock(self, z, eplus):
        



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