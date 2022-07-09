# Sala-i_Martin (1996)的数学推导细节
## 1.家庭部门


```maple
# Assumptions
restart:
assumption_utility:= u(c[y,t]) = ln(c[y,t]), u(c[o,t+1]) = ln(c[o,t+1]):
assumption_discount:= Psi=rho:
assumption_n := n=0:
```


    kilobytes used=2797, alloc=9776, time=0.55



```maple
# agent' lifetime utility
utility := subs(assumption_utility,u(c[y,t])+1/(1+rho)*u(c[o,t+1]));
```


    kilobytes used=5904, alloc=9776, time=0.98





$$\ln \left(c_{y ,t}\right)+\frac{\ln \left(c_{o ,t +1}\right)}{1+\rho}$$




```maple
# agent's young-age consumption flow constraint
consumption_y := c[y,t]=w[y,t]*l[y,t]*(1-tau)+b[t]-s[t];
```




$$c_{y ,t} = w_{y ,t} l_{y ,t} \left(1-\tau \right)+b_{t}-s_{t}$$




```maple
# agent's old-age consumption flow constraint
consumption_o := subs(assumption_n,c[o,t+1]=w[o,t+1]*l[o,t+1]+T[t+1]+s[t]*r[t+1]-(1+n)*b[t+1]);
```




$$c_{o ,t +1} = w_{o ,t +1} l_{o ,t +1}+s_{t} r_{t +1}+T_{t +1}-b_{t +1}$$




```maple
# reduced agent's lifetime utility by incorporating with budget constraints
reduced_utility:=subs(consumption_y,consumption_o,utility)
```




$$\ln \left(w_{y ,t} l_{y ,t} \left(1-\tau \right)+b_{t}-s_{t}\right)+\frac{\ln \left(w_{o ,t +1} l_{o ,t +1}+s_{t} r_{t +1}+T_{t +1}-b_{t +1}\right)}{1+\rho}$$




```maple
# bellman equation 
bellman := subs(assumption_discount,V(b[t])=reduced_utility+1/(1+Psi)*V(b[t+1]));
```




$$V \left(b_{t}\right) = \ln \left(w_{y ,t} l_{y ,t} \left(1-\tau \right)+b_{t}-s_{t}\right)+\frac{\ln \left(w_{o ,t +1} l_{o ,t +1}+s_{t} r_{t +1}+T_{t +1}-b_{t +1}\right)}{1+\rho}+\frac{V \left(b_{t +1}\right)}{1+\rho}$$




```maple
# optimal condition for saving s[t]
foc_s := diff(bellman,s[t]):
sub_rule_s:= rhs(consumption_y)=lhs(consumption_y),rhs(consumption_o)=lhs(consumption_o):
optimal_s := subs(sub_rule_s,foc_s);
```




$$0 = -\frac{1}{c_{y ,t}}+\frac{r_{t +1}}{\left(1+\rho \right) c_{o ,t +1}}$$




```maple
# well-formated optimal condition for saving s[t]
optimal_s_well:=isolate(optimal_s,-op(1,rhs(optimal_s)));
```




$$\frac{1}{c_{y ,t}} = \frac{r_{t +1}}{\left(1+\rho \right) c_{o ,t +1}}$$




```maple
# optimal condition for bequest b[t+1]
## first-order condition for b[t+1]
foc_b := subs(rhs(consumption_o)=lhs(consumption_o),convert(diff(bellman, b[t+1]),D));
```




$$0 = -\frac{1}{\left(1+\rho \right) c_{o ,t +1}}+\frac{D\left(V \right)\left(b_{t +1}\right)}{1+\rho}$$




```maple
## envelop condition for b[t+1]
envelope_b := subs(rhs(consumption_y)=lhs(consumption_y),t=t+1,convert(diff(bellman,b[t]),D));
```




$$D\left(V \right)\left(b_{t +1}\right) = \frac{1}{c_{y ,t +1}}$$




```maple
## optimal condition for bequest b[t+1]
optimal_b := subs(envelope_b,foc_b);
```




$$0 = -\frac{1}{\left(1+\rho \right) c_{o ,t +1}}+\frac{1}{\left(1+\rho \right) c_{y ,t +1}}$$




```maple
# well-formated optimal condition for bequest b[t+1]
optimal_b_well:=(1+rho)*isolate(optimal_b,-op(1,rhs(optimal_b)));
```




$$\frac{1}{c_{o ,t +1}} = \frac{1}{c_{y ,t +1}}$$




```maple
# analytic solution of saving s[t]

```

## 2. 生产部门


```maple
# firm j's production function
production := Y[t] = A*K[t]^alpha*(H[t])^(1-alpha)*(H[t]/N[t])^epsilon[j]*(H[a,t]/N[a,t])^epsilon;
```




$$Y_{t} = A K_{t}^{\alpha} H_{t}^{1-\alpha} \left(\frac{H_{t}}{N_{t}}\right)^{\epsilon_{j}} \left(\frac{H_{a ,t}}{N_{a ,t}}\right)^{\epsilon}$$




```maple
# firm j's effective labor
effective_labor := H[t] = n[y,t]*h[y,t]+n[o,t]*h[o,t];
```




$$H_{t} = n_{o ,t} h_{o ,t}+n_{y ,t} h_{y ,t}$$




```maple
# firm j's employment
employment := N[t] = n[y,t]+n[o,t];
```




$$N_{t} = n_{y ,t}+n_{o ,t}$$




```maple
# firm's reduced-form production function 
reduced_production := subs(effective_labor, employment,production);
```




$$Y_{t} = A K_{t}^{\alpha} \left(n_{o ,t} h_{o ,t}+n_{y ,t} h_{y ,t}\right)^{1-\alpha} \left(\frac{n_{o ,t} h_{o ,t}+n_{y ,t} h_{y ,t}}{n_{y ,t}+n_{o ,t}}\right)^{\epsilon_{j}} \left(\frac{H_{a ,t}}{N_{a ,t}}\right)^{\epsilon}$$




```maple
# young-age human capital accumlation
human_capital_y:= h[y,t+1] = (1+gamma)*h[y,t];
```




$$h_{y ,t +1} = \left(1+\gamma \right) h_{y ,t}$$




```maple
# old-age human capital depreciation
human_capital_o:= h[o,t+1] = (1-delta(h[y,t]))*h[y,t];
```




$$h_{o ,t +1} = \left(1-\delta \left(h_{y ,t}\right)\right) h_{y ,t}$$




```maple
# profit flow of firm
profit := pi[t] = rhs(reduced_production)-r[t]*K[t]-w[y,t]*n[y,t]-w[o,t]*n[o,t];
```




$$\pi_{t} = A K_{t}^{\alpha} \left(n_{o ,t} h_{o ,t}+n_{y ,t} h_{y ,t}\right)^{1-\alpha} \left(\frac{n_{o ,t} h_{o ,t}+n_{y ,t} h_{y ,t}}{n_{y ,t}+n_{o ,t}}\right)^{\epsilon_{j}} \left(\frac{H_{a ,t}}{N_{a ,t}}\right)^{\epsilon}-r_{t} K_{t}-w_{y ,t} n_{y ,t}-w_{o ,t} n_{o ,t}$$




```maple
# foc of capital K[t]
raw_foc_k := diff(profit,K[t]):
foc_k := algsubs(rhs(reduced_production)=lhs(reduced_production),raw_foc_k);
```




$$0 = \frac{\alpha  Y_{t}-r_{t} K_{t}}{K_{t}}$$




```maple
# interest rate 
interest:=isolate(foc_k,r[t]);
```




$$r_{t} = \frac{\alpha  Y_{t}}{K_{t}}$$




```maple
# foc of young-age employment
raw_foc_ly := diff(profit,n[y,t]):
foc_ly := lhs(raw_foc_ly)=algsubs(rhs(reduced_production)=lhs(reduced_production),op(1,rhs(raw_foc_ly)))+algsubs(rhs(reduced_production)=lhs(reduced_production),op(2,rhs(raw_foc_ly)))+op(3,rhs(raw_foc_ly)):
```


```maple
# young-age wage rate
wage_y := isolate(foc_ly,w[y,t]);
```




$$w_{y ,t} = -\frac{\left(-1+\alpha \right) h_{y ,t} Y_{t}}{n_{o ,t} h_{o ,t}+n_{y ,t} h_{y ,t}}-\frac{Y_{t} \left(h_{o ,t}-h_{y ,t}\right) n_{o ,t} \epsilon_{j}}{\left(n_{o ,t} h_{o ,t}+n_{y ,t} h_{y ,t}\right) \left(n_{y ,t}+n_{o ,t}\right)}$$




```maple
# foc of old-age employment
raw_foc_lo := diff(profit,n[o,t]):
foc_lo := lhs(raw_foc_lo)=algsubs(rhs(reduced_production)=lhs(reduced_production),op(1,rhs(raw_foc_lo)))+algsubs(rhs(reduced_production)=lhs(reduced_production),op(2,rhs(raw_foc_lo)))+op(3,rhs(raw_foc_lo)):
```


```maple
# old-age wage rate
wage_o := isolate(foc_lo,w[o,t]);
```




$$w_{o ,t} = -\frac{\left(-1+\alpha \right) h_{o ,t} Y_{t}}{n_{o ,t} h_{o ,t}+n_{y ,t} h_{y ,t}}+\frac{Y_{t} \left(h_{o ,t}-h_{y ,t}\right) n_{y ,t} \epsilon_{j}}{\left(n_{o ,t} h_{o ,t}+n_{y ,t} h_{y ,t}\right) \left(n_{y ,t}+n_{o ,t}\right)}$$




```maple
# factor income distribution
income := n[o,t]*lhs(wage_o)+n[y,t]*lhs(wage_y)+K[t]*lhs(interest)=n[o,t]*rhs(wage_o)+n[y,t]*rhs(wage_y)+K[t]*rhs(interest):
income := simplify(income);
```




$$r_{t} K_{t}+w_{o ,t} n_{o ,t}+w_{y ,t} n_{y ,t} = Y_{t}$$



## 3. 政府部门


```maple
# social security system
social_security := T[t+1]=tau*w[y,t+1]*l[y,t+1];
```




$$T_{t +1} = \tau  w_{y ,t +1} l_{y ,t +1}$$



## 3. 一般均衡


```maple
# capital market clear
clear_k:= K[t+1]=s[t];
```




$$K_{t +1} = s_{t}$$




```maple
# young-age labor market clear
clear_ny := n[y,t]=l[y,t];
```




$$n_{y ,t} = l_{y ,t}$$




```maple
# old-age labor market clear
clear_oy := n[o,t]=l[o,t];
```




$$n_{o ,t} = l_{o ,t}$$




```maple
# symmetric condition of H[a,t]
symmetric_h:= subs(effective_labor,H[a,t]=H[t]);
```




$$H_{a ,t} = n_{o ,t} h_{o ,t}+n_{y ,t} h_{y ,t}$$




```maple
# symmetric condition of N[a,t]
symmetric_n:= subs(employment,N[a,t]=N[t]);
```




$$N_{a ,t} = n_{y ,t}+n_{o ,t}$$



## 4. 分析结果


```maple
# 求解储蓄率
# lifetime budget constraint
optimal_s_real := subs(subs(t=t+1,interest),optimal_s_well);
```




$$\frac{1}{c_{y ,t}} = \frac{\alpha  Y_{t +1}}{\left(1+\rho \right) K_{t +1} c_{o ,t +1}}$$




```maple
# guess constant consumption rate c[y,t]=c[y]*Y[t], c[o,t+1]=c[o]*Y[t+1] , c[y,t+1]=c[y]*Y[t+1]
guess := c[y,t]=c[y]*Y[t], c[o,t+1]=c[o]*Y[t+1], c[y,t+1]=c[y]*Y[t+1]:
optimal_s_ratio:=subs(guess,optimal_s_real);
```




$$\frac{1}{c_{y} Y_{t}} = \frac{\alpha}{\left(1+\rho \right) K_{t +1} c_{o}}$$




```maple
# guess constant consumption rate c[y,t]=c[y]*Y[t], c[o,t+1]=c[o]*Y[t+1] , c[y,t+1]=c[y]*Y[t+1]
optimal_b_ratio:=Y[t+1]*subs(guess,optimal_b_well);
```




$$\frac{1}{c_{o}} = \frac{1}{c_{y}}$$




```maple
# solution of K[t+1]
solution_k:=K[t+1]=solve(subs(optimal_b_ratio,optimal_s_ratio),K[t+1]);
```




$$K_{t +1} = \frac{\alpha  Y_{t}}{1+\rho}$$




```maple
# dynamics of output Y[t+1] without social security n[o,t]>0
production_work := subs(t=t+1,solution_k,subs(t=t+1,symmetric_h),subs(t=t+1,symmetric_n),reduced_production);
```




$$Y_{t +1} = A \left(\frac{\alpha  Y_{t}}{1+\rho}\right)^{\alpha} \left(h_{o ,t +1} n_{o ,t +1}+h_{y ,t +1} n_{y ,t +1}\right)^{1-\alpha} \left(\frac{h_{o ,t +1} n_{o ,t +1}+h_{y ,t +1} n_{y ,t +1}}{n_{y ,t +1}+n_{o ,t +1}}\right)^{\epsilon_{j}} \left(\frac{h_{o ,t +1} n_{o ,t +1}+h_{y ,t +1} n_{y ,t +1}}{n_{y ,t +1}+n_{o ,t +1}}\right)^{\epsilon}$$




```maple
production_retire:=subs(t=t+1,solution_k,subs(t=t+1,symmetric_h),subs(t=t+1,symmetric_n),n[o,t+1]=0,Y[t+1]=Y[s,t+1],Y[t]=Y[s,t],reduced_production);
```




$$Y_{s ,t +1} = A \left(\frac{\alpha  Y_{s ,t}}{1+\rho}\right)^{\alpha} \left(h_{y ,t +1} n_{y ,t +1}\right)^{1-\alpha} h_{y ,t +1}^{\epsilon_{j}} h_{y ,t +1}^{\epsilon}$$




```maple
# output with elderly labor
bgp := delta(h[y,t])=delta,n[o,t+1]=n[o],n[y,t+1]=n[y]:
output_dynamics_work:=simplify(subs(human_capital_y,human_capital_o,bgp,production_work),power,symbolic):
output_dynamics_work:=simplify(ln(lhs(output_dynamics_work))=ln(rhs(output_dynamics_work)),power,symbolic);
```




$$\ln \left(Y_{t +1}\right) = \ln \left(A \right)+\alpha  \ln \left(\alpha \right)+\alpha  \ln \left(Y_{t}\right)-\alpha  \ln \left(1+\rho \right)+\left(1-\alpha +\epsilon_{j}+\epsilon \right) \ln \left(h_{y ,t}\right)+\left(1-\alpha +\epsilon_{j}+\epsilon \right) \ln \left(n_{y} \left(1+\gamma \right)-n_{o} \left(\delta -1\right)\right)+\left(-\epsilon_{j}-\epsilon \right) \ln \left(n_{y}+n_{o}\right)$$




```maple
# output without elderly labor
output_dynamics_retire:=simplify(subs(human_capital_y,human_capital_o,bgp,production_retire),power,symbolic):
output_dynamics_retire:=simplify(ln(lhs(output_dynamics_retire))=ln(rhs(output_dynamics_retire)),power,symbolic);
```




$$\ln \left(Y_{s ,t +1}\right) = \ln \left(A \right)+\alpha  \ln \left(\alpha \right)+\alpha  \ln \left(Y_{s ,t}\right)-\alpha  \ln \left(1+\rho \right)+\left(1-\alpha +\epsilon_{j}+\epsilon \right) \ln \left(1+\gamma \right)+\left(1-\alpha +\epsilon_{j}+\epsilon \right) \ln \left(h_{y ,t}\right)+\left(1-\alpha \right) \ln \left(n_{y}\right)$$




```maple
# well-format output dynamics with elderly labor
constant_work := eta[w]=rhs(output_dynamics_work)-alpha*ln(Y[t])-(1-alpha+epsilon[j]+epsilon)*ln(h[y,t]):
output_dynamics_work := lhs(output_dynamics_work)=alpha*ln(Y[t])+(1-alpha+epsilon[j]+epsilon)*ln(h[y,t])+lhs(constant_work);
```




$$\ln \left(Y_{t +1}\right) = \alpha  \ln \left(Y_{t}\right)+\left(1-\alpha +\epsilon_{j}+\epsilon \right) \ln \left(h_{y ,t}\right)+\eta_{w}$$




```maple
# well-format output dynamics with elderly labor
constant_retire := eta[r]=rhs(output_dynamics_retire)-alpha*ln(Y[s,t])-(1-alpha+epsilon[j]+epsilon)*ln(h[y,t]):
output_dynamics_retire := lhs(output_dynamics_retire)=alpha*ln(Y[s,t])+(1-alpha+epsilon[j]+epsilon)*ln(h[y,t])+lhs(constant_retire);
```




$$\ln \left(Y_{s ,t +1}\right) = \alpha  \ln \left(Y_{s ,t}\right)+\left(1-\alpha +\epsilon_{j}+\epsilon \right) \ln \left(h_{y ,t}\right)+\eta_{r}$$



此时，由于两种动态，仅仅常数项不同，因此，BGP的增长率是相同的，均为$\frac{1-\alpha+\epsilon_{j}+\epsilon}{1-\alpha}\gamma$(由于$h_{y,t}$的增长率是常数\gamma)


```maple
# The difference of output under two cases
lhs(output_dynamics_work)-lhs(output_dynamics_retire)=rhs(output_dynamics_work)-rhs(output_dynamics_retire);
```




$$\ln \left(Y_{t +1}\right)-\ln \left(Y_{s ,t +1}\right) = \alpha  \ln \left(Y_{t}\right)+\eta_{w}-\alpha  \ln \left(Y_{s ,t}\right)-\eta_{r}$$



从上面可知，稳态的产出差将等于$\Delta_{Y}\equiv (\ln Y - \ln Y_{s})^{*}=\frac{\eta_{w}-\eta_{r}}{1-\alpha}$


```maple
# The steady-state difference of output under two cases
output_gap:=Delta[Y]= (eta[w]-eta[r])/(1-alpha):
output_gap:= expand(subs(constant_retire,constant_work,output_gap));
```




$$\Delta_{Y} = \frac{\ln \left(n_{y} \left(1+\gamma \right)-n_{o} \left(\delta -1\right)\right)}{1-\alpha}-\frac{\ln \left(n_{y} \left(1+\gamma \right)-n_{o} \left(\delta -1\right)\right) \alpha}{1-\alpha}+\frac{\ln \left(n_{y} \left(1+\gamma \right)-n_{o} \left(\delta -1\right)\right) \epsilon_{j}}{1-\alpha}+\frac{\ln \left(n_{y} \left(1+\gamma \right)-n_{o} \left(\delta -1\right)\right) \epsilon}{1-\alpha}-\frac{\ln \left(n_{y}+n_{o}\right) \epsilon_{j}}{1-\alpha}-\frac{\ln \left(n_{y}+n_{o}\right) \epsilon}{1-\alpha}-\frac{\ln \left(1+\gamma \right)}{1-\alpha}+\frac{\ln \left(1+\gamma \right) \alpha}{1-\alpha}-\frac{\ln \left(1+\gamma \right) \epsilon_{j}}{1-\alpha}-\frac{\ln \left(1+\gamma \right) \epsilon}{1-\alpha}-\frac{\ln \left(n_{y}\right)}{1-\alpha}+\frac{\ln \left(n_{y}\right) \alpha}{1-\alpha}$$




```maple
output_gap:=lhs(output_gap)=simplify(op(1,rhs(output_gap))+op(2,rhs(output_gap))+op(3,rhs(output_gap))+op(4,rhs(output_gap)))+simplify(op(5,rhs(output_gap))+op(6,rhs(output_gap)))+simplify(op(7,rhs(output_gap))+op(8,rhs(output_gap))+op(9,rhs(output_gap))+op(10,rhs(output_gap)))+simplify(op(11,rhs(output_gap))+op(12,rhs(output_gap)));
```




$$\Delta_{Y} = \frac{\left(-1+\alpha -\epsilon_{j}-\epsilon \right) \ln \left(n_{y} \left(1+\gamma \right)-n_{o} \left(\delta -1\right)\right)}{-1+\alpha}+\frac{\left(\epsilon_{j}+\epsilon \right) \ln \left(n_{y}+n_{o}\right)}{-1+\alpha}-\frac{\left(-1+\alpha -\epsilon_{j}-\epsilon \right) \ln \left(1+\gamma \right)}{-1+\alpha}-\ln \left(n_{y}\right)$$




```maple
output_gap:=lhs(output_gap)=simplify(op(1,rhs(output_gap))+op(3,rhs(output_gap)))+simplify(op(2,rhs(output_gap))+op(4,rhs(output_gap)));
```




$$\Delta_{Y} = \frac{\left(-1+\alpha -\epsilon_{j}-\epsilon \right) \left(\ln \left(n_{y} \left(1+\gamma \right)-n_{o} \left(\delta -1\right)\right)-\ln \left(1+\gamma \right)\right)}{-1+\alpha}+\frac{\left(\epsilon_{j}+\epsilon \right) \ln \left(n_{y}+n_{o}\right)}{-1+\alpha}-\ln \left(n_{y}\right)$$




```maple
# in the absence of human capital externality
externality_no := epsilon[j]=0,epsilon=0:
output_gap_noexternality:=subs(externality_no,Delta[Y]=Delta[Y,noex],output_gap);
```




$$\Delta_{Y ,\mathit{noex}} = \ln \left(n_{y} \left(1+\gamma \right)-n_{o} \left(\delta -1\right)\right)-\ln \left(1+\gamma \right)-\ln \left(n_{y}\right)$$



即，没有人力资本外部性，老年工作比退休具有更高的稳态产出，因为$\Delta_{Y,noex}=\ln(1+\frac{n_{o}(1-\delta)}{n_{y}(1+\gamma)})>0$恒成立。


```maple
# in the presence of sufficiently large human capital externality and human capital depreciation 
## epsilon[j]=1,epsilon=0, delta=1
externality_yes := epsilon[j]=1,epsilon=0,delta=1:
output_gap_externality:=simplify(subs(externality_yes,Delta[Y]=Delta[Y,ex],output_gap),power,symbolic);
```




$$\Delta_{Y ,\mathit{ex}} = \frac{-\ln \left(n_{y}\right)+\ln \left(n_{y}+n_{o}\right)}{-1+\alpha}$$



即，足够大的人力资本外部性和人力资本折旧率，老年工作比退休具有更低的稳态产出，因为$\Delta_{Y,ex}=-\frac{\ln[1+n_{o}/n_{y}]}{1-\alpha}<0$成立。
