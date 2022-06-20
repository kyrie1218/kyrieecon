##### 跨期替代弹性
所谓跨期替代弹性$\sigma_{X}$是指变量$X_{t}$在$t$期和$t+1$之间的相对水平$X_{t+1}/X_{t}$随相对价格$P(X_{t+1})/P(X_{t})$的反向变动程度（以各自的百分比衡量）。即有
$$
\partial \ln \frac{X_{t+1}}{X_{t}}=-\sigma_{X} \partial \ln \frac{P(X_{t+1})}{P(X_{t})}
$$

> [!Tip] 
> (**跨期消费替代弹性**) 给定CRRA效用函数$U(C_{t})=\frac{C_{t}^{1-\theta}-1}{1-\theta}$，则消费的跨期替代弹性$\sigma_{C}$计算如下：
>$$\sigma_{C} \equiv -\frac{\partial \ln \frac{C_{t+1}}{C_{t}}}{\partial \ln \frac{U'(C_{t+1})}{U'(C_{t})}}=-\frac{\partial \ln \frac{C_{t+1}}{C_{t}}}{\partial \ln (\frac{C_{t+1}}{C_{t}})^{-\theta}}=1/\theta$$
> 其中，消费者均衡时的价格体现为消费的边际效用。

##### 李嘉图等价

##### python类的初始化方法
>[!Tip]
> 在定义一个python类的时候，我们需要对其初始化，使用`__init__`这个> 初始化方法。这个方法有如下几个特点:
>- 在实例化对象时,默认会自动调用这个初始化方法;
>- 定义__init__方法时,不能使用return;
>- 一般用于存放类的属性,如类名,公共参数值,打印一些问候信息。

##### kwargs.get方法
该方法用于设置默认的可选关键词参数，即如果该关键词参数没有赋值，则使用其中的默认参数。例如：
```
self.stochastic = kwargs.get('stochastic',False)
```
这意味着如果关键词参数stochastic没有设置，则默认为`stochastic=False`，此时，实例属性`self.stochastic = False`。


##### Python中的None值
None是python中的一个常量，代表真空状态，没有输出，一般可作为占位符。

##### Python中的assert语句
assert语句用于条件判断是否声明内容为真，如果为真，则继续运行，否则，将导致程序因异常而中断。

##### np.random.seed方法
该方法是Numpy中的一个方法，用于设置随机数的序号，该序号可以用于重复原来的随机结果。

##### Python中的pass语句
pass语句用于语法结构的占位，例如：
```python
def fun(x):
    pass
```
这时，函数fun没有定义具体操作，仅用pass占位，以防止运行错误。


##### Python中的copy方法
如果对一个字典`dict`应用`copy`方法，及使用`dict.copy()`，那么我们实际上对其字典`dict`进行了怎么样的操作呢？

答案：浅复制一个相同的字典，但与直接赋值有些区别。区别在于后者会随被复制字典的数据变动而变动，而前者不会。例如：
```python
dict1 =  {'user':'kyrie'}
 
dict2 = dict1          # 直接赋值
dict3 = dict1.copy()   # copy方法
 
# 修改 data 数据
dict1['user']='root'
# 输出结果
print(dict1)
print(dict2)
print(dict3)
```
结果如下：
```
{'user': 'root'}
{'user': 'root'}
{'user': 'kyrie'}
```


