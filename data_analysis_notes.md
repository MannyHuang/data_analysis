## Python
### 删除列数据空格
str.strip()会删除*数字型*数据和字符*左右两侧*的空格
df['Chinese'] = [' 1 $','2,',1,2]
df['Chinese] = df['Chinese].str.strip()
result: 1 $,2,NAN,NAN

使用map（str.strip）则要求[' 1 $','2,',1,2]*均为str*
df['Chinese'] = [' 1 $','2,','1','2']
result: 1 $,2,1,2

### 空值的不同表示
b = 1
b = None
print(b) None
b = np.nan
print(b) nan

DataFrame中
df['Chinese'] = [' 1 $','2,',None,np.nan]
result: 1 $,2,None,NaN
None 显示None
np.nan 显示NaN

Int元素设为空值会报错
a = np.arange（10）
a[2] = np.nan / None 报错
原因：None的class是 type(None): <class 'NoneType'> 
np.nan的class是 type(np.nan): <class 'float'> Numpy数组中，一般而言，int元素赋值为float类型是不合法的，但不会报错，会自动转换为int类型

Int元素设为空值不会报错
a = np.arange（10,dtype=float）
a[2] = np.nan
a[3] = None
result: [0. 1. nan nan 4. 5. 6. 7. 8. 9.]在numpy中都以nan形式出现


### apply
axis：0 行操作 1 列操作
args：(x1, x2, ...)


### 数据统计
Pandas 和 NumPy 一样，都有常用的统计函数，如果遇到空值 NaN，会自动排除

### 数据表的合并 pd.merge()
- 指定列连接 
df3 = pd.merge(df1, df2, on='name')  合并df1和df2的name相同的行
- inner 内链接
df3 = pd.merge(df1, df2, how='inner') inner 内链接是 merge 合并的默认情况，inner 内连接其实也就是键的交集，在这里 df1, df2 相同的键是 name，所以是基于 name 字段做的连接：
- left 左连接
df3 = pd.merge(df1, df2, how='left') 以第一个 DataFrame 为主进行的连接，第二个 DataFrame 作为补充
- right 右连接
df3 = pd.merge(df1, df2, how='right') 以第二个 DataFrame 为主进行的连接，第一个 DataFrame 作为补充 
- outer 外连接
df3 = pd.merge(df1, df2, how='outer') 两个 DataFrame 的并集


### from pandasql import sqldf



