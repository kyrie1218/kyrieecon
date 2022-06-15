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

