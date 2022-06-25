# Pandas： Dataframe处理利器

## 1. 简介
Pandas是一个用于创建以及处理dataframe（面板数据集）的python库。本文使用1.3.4版本。详细使用方法参考[Pandas1.3 API参考手册](https://pandas.pydata.org/pandas-docs/version/1.3/reference/frame.html)。

## 2. 一个简单的例子
```python
import pandas as pd # 导入pandas库并命名为pd

# 导入目录`/home/kyrie/data`下的test.dta文件为dataframe; 
# 并命名该dataframe为df_test;
df_test = pd.read_stata('/home/kyrie/data/test.dta') 

df_test.head(5) # 展示df_test的前五行
```

## 3. 专题
### 3.1 筛选行
#### 3.1.1 按条件筛选行 `query`
```python
# 单条件
df_test.query("inw4=='1.yes'")  # 仅包含inw4=='1.yes'的行

# 多条件
df_test.query("inw4=='1.yes' and h4child>0") # 仅包含inw4=='1.yes'且h4child>0的行
```

>[!Note] df.query方法包含两个重要参数：一个字符串格式的表达式`expr`，一个布尔类型的关键词参数`inplace`：
> - `expr`参数用于限定行满足的条件，表达式左边一般为df中的单个列名，表达式右边一般为单个值或者df的另一个列名; *注意：(1) 如果需要使用df之外的变量，则需要在df之外的变量名前加美元符号`@`来引用; (2) 如果您的df列名不符合python的变量名命名规则，如包含空格等，则需要将这种非法列名使用双反引号``括起来。*
> - `inplace`关键词参数默认为`False`，这将返回一个被query后的df副本; 如果选`True`，则将修改原始的df，且不会返回任何东西。

#### 3.2 筛选列
#### 3.2.1 按列名筛选列 `filter`
