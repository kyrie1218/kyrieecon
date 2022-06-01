## 1. 核心机制
## 2. 模型细节
### 2.1 最终产品部门
最终产品部门设置与Rivera-Batiz and Romer, 1991一致。
$$
Y_{t} = \hat{A}L^{1/\sigma}\{\int_{0}^{N_{t}}[x_{t}(z)]^{1-1/\sigma}dz\}
$$

其中$Y_{t}$为最终产出；$\hat{A}$代表最终生产部门的全要素生产率；$L$是劳动;$x_{t}(z)$代表$t$期的中间产品$z$的产量;$N_{t}$代表中间产品的种类，它的变动提前技术前沿的变动。
> [!Note]
> - 劳动和中间产品是C-D组合形式，因而是要素互补的, 劳动收入份额则为$1/\sigma$；
> - 中间产品之间是CES组合形式，说明中间产品的 跨期替代弹性 是可变的，中间产品替代弹性为$\sigma$。
> - CES函数指数是$1-1/\sigma$，各种类的份额比$1:1$，因此，该函数对应的替代弹性为$1*[-(1-1/\sigma-1)]=\sigma$.
> - 单种中间品的需求价格弹性是$\sigma$: $-\frac{\partial \ln x(z)}{\partial \ln Y_{x(z)}}=\sigma$.

### 2.2 中间资本品生产部门
**本文创新：** 有限期的中间品生产垄断，即老产品$z \in [0,N_{t-1}]$完全竞争生产，新产品$z \in [N_{t-1},N_{t}]$ 垄断生产。
其他的设定和[[Rivera-Batiz and Romer (1991)]]一致。研发需要消耗$F$单位的资本，中间品生产则需要每单位中级品消耗$a$单位的资本。当资本价格为$r_{t}$时， 研发和中间品生产的边际成本则分别为$Fr_{t},\,ar_{t}$.

自然，完全竞争下的老产品的价格为

$$
p_{t}(z)\equiv p_{t}^{c}=ar_{t}
$$

而垄断生产的新产品为根据边际成本加成定价，加成比例根据中间品的需求价格弹性而定，即新产品的价格为
$$
p_{t}(z)\equiv p_{t}^{m}=ar_{t}(1+\frac{1}{\sigma-1})=a\sigma r_{t}/(\sigma-1)
$$

另外，根据生产函数，我们可以获得中间品的相对比例（新和旧产品之间）：

$$
\frac{x_{t}^{c}}{x_{t}^{m}}=[\frac{p_{t}^{c}}{p_{t}^{m}}]^{-\sigma}=[1-\frac{1}{\sigma}]^{-\sigma}
$$

### 2.3 中间资本品研发部门
创新者为了追求边际垄断利润最大化（注意：利润仅能维持一期）：

$$
\pi_{t} = p_{t}^{m}x_{t}^{m}-r_{t}(ax_{t}^{m}+F);
$$

由于研发活动是free entry的，因此，只有垄断利润为0的时候，研发研发部门才会均衡。即对于新的中间品种类$N_{t}\geq N_{t-1}$, 要么边际垄断利润为负，没有新研发；要么边际垄断利润为0,新产品产生。注意：由于资本价格为正，带入新中间产品需求函数可简化为如下条件：

$$
a x_{t}^{m} \leq (\sigma-1)F,\, N_{t}\leq N_{t-1},\, (ax_{t}^{m}-(\sigma-1)F)(N_{t}-N_{t-1})=0
$$

这说明，存在交点解，即没有新产品出现的情形，即$ax_{t}^{m}<(\sigma-1)F,\quad N_{t}=N_{t-1}$.

### 2.4 家庭部门
本文做了简化处理，和solow模型一样，假定外生储蓄率$\mu$.
即储蓄为$K_{t}=\mu Y_{t}$.

此时，人均资本存量$k_{t}=K_{t}/(\theta \sigma F)N_{t}$呈现如下动态：

$$
k_{t} =\begin{cases} G k_{t-1}^{1-1/\sigma},& \quad k_{t-1} \leq 1 ,\, G\equiv \mu A\\ \frac{G k_{t-1}}{1+\theta(k_{t-1}-1)},& \quad k_{t-1} \geq 1\end{cases}
$$
### 2.5 一般均衡
资本市场出清（资本将用于生产旧产品和研发新产品）

$$
K_{t-1} = N_{t-1}ax_{t}^{c}+(N_{t}-N_{t-1})(ax_{t}^{m}+F)
$$

研发均衡（要么$N_{t}=N_{t-1}$,要么$ax_{t}^{m}=(\sigma-1)F$)意味着资本市场出清可重写为

$$
ax_{t}^{c}=\frac{K_{t-1}}{N_{t-1}},\, when \,N_{t}=N_{t-1}
$$

$$
ax_{t}^{c}= \theta \sigma F,\, when\, ax_{t}^{m}=(\sigma-1)F, \theta \equiv [1-\frac{1}{\sigma}]^{1-\sigma}
$$

此时，技术前沿动态可以表示为：

$$
N_{t}=N_{t-1}+\max\{0,\frac{K_{t-1}}{\sigma F}-\theta N_{t-1}\}
$$

这个实在体现出技术进步的停滞或者继续的可能性均存在，是否技术进步将取决于两个重要参数：$\sigma$和$F$. 当研发成本$F$足够高，则不会进行研发；当中间派需求价格弹性$\sigma$越高，也会倾向于不研发。

此时，回看总量生产函数：
当$N_{t}=N_{t-1}$时，有

$$
Y_{t} =\begin{cases} A[\theta \sigma F N_{t-1}]^{1/\sigma}[K_{t-1}]^{1-(1/\sigma)} ,& \quad K_{t-1} \leq \theta \sigma F N_{t-1} \\ AK_{t-1},& \quad K_{t-1}\geq \theta \sigma F N_{t-1}\end{cases}
$$

其中，$A\equiv \frac{\hat{A}}{a}[\frac{aL}{\theta \sigma F}]^{1/\sigma}$.

注意：以上刻画了上一期资本存量配置对下一期产出的影响。这个可以体现出周期特征。但周期的特征则需要进一步刻画资本积累的，即本期产出用于资本的份额。

## 3. 基本结果
注意：当$G>1$时，则存在内生增长并包含周期。

![图1： 转移动态图](https://raw.githubusercontent.com/kyrie1218/picgo/main/img/Screenshot-4.png)

## 参考文献
[1] Matsuyama, K. (1999). Growing Through Cycles. Econometrica, 67(2), 335–347. https://doi.org/10.1111/1468-0262.00021

[2] Matsuyama, K. (2001). Growing through Cycles in an Infinitely Lived Agent Economy. Journal of Economic Theory, 100(2), 220–234. https://doi.org/10.1006/jeth.2000.2770