# coding=utf-8
# 字符串格式化,%操作符
print("I'm %s. I'm %d year old" % ('Vamei', 99));
print("I'm %(name)s. I'm %(age)d year old" % {'name': 'Vamei', 'age': 99});
'''
格式符
格式符为真实值预留位置，并控制显示的格式。格式符可以包含有一个类型码，用以控制显示的类型，如下:

%s    字符串 (采用str()的显示)
%r    字符串 (采用repr()的显示)
%c    单个字符
%b    二进制整数
%d    十进制整数
%i    十进制整数
%o    八进制整数
%x    十六进制整数
%e    指数 (基底写为e)
%E    指数 (基底写为E)
%f    浮点数
%F    浮点数，与上相同
%g    指数(e)或浮点数 (根据显示长度)
%G    指数(E)或浮点数 (根据显示长度)
%%    字符"%"
可以用如下的方式，对格式进行进一步的控制：
%[(name)][flags][width].[precision]typecode
(name)为命名
flags可以有+,-,' '或0。+表示右对齐。-表示左对齐。' '为一个空格，表示在正数的左侧填充一个空格，从而与负数对齐。0表示使用0填充。
width表示显示宽度
precision表示小数点后精度
'''

# 数组
'''
(1) list 普通的链表，初始化后可以通过特定方法动态增加元素。
定义方式：arr = [元素]

(2) Tuple 固定的数组，一旦定义后，其元素个数是不能再改变的。
定义方式：arr = (元素)

(2) Dictionary 词典类型， 即是Hash数组。
定义方式：arr = {元素k:v}

del 语句 和 : 的用法
可以用 start : end 表示数组里的一个区间 ( i >= start and i < end)
del 删除数组里的指定元素
如： del arr[0]
del arr[0, 2]
newarr = arr[0, 2]

d、遍历数组：
for k, v in enumerate(arr):
print k, v

e、增加元素：
一维
arr.append('aaa')
二维
arr[0].append('aaa')
如果要在任意位置插入用 arr.insert(n, 值)
此外还有一种特殊的用法是：
arr += [数组元素]
在不指定下标的情况下，是允许用 += 增加数组元素的。

Tuple 固定数组
Tuple 是不可变 list，一旦创建了一个 tuple 就不能以任何方式改变它。
Tuple 可以转换成 list， 反之亦然。
Tuple 比 list 操作速度快。如果您定义了一个值的常量集, 并且唯一要用它做的是不断地遍历它, 请使用 tuple 代替 list。
转换方式为：
t = list( t )
反之：
arr = tuple( arr )

Dictionary (哈希数组)词典数组

#Dictionary 的用法比较简单，它可以存储任意值，并允许是不同类型的值，下面实例来说明：
#下面例子中 a 是整数， b 是字符串, c 是数组，这个例子充分说明哈希数组的适用性。
dict_arr = {'a': 100, 'b':'boy', 'c':['o', 'p', 'q']}

#可以直接增加一个元素，如果同名，则会改变原来的key的元素的值
dict_arr['d'] = 'dog'

#输出所有的key
print dict_arr.keys()

#输出所有的value
print dict_arr.values()

#遍历数组
import types
for k in dict_arr:
v = dict_arr.get(k)
if type(v) is types.ListType: #如果数据是list类型，继续遍历
print k, '---'
for kk, vv in enumerate(v):
print kk, vv
print '---'
else:
print dict_arr.get(k)
'''


# 日期
'''
 在datetime模块中有一个timedelta这个方法，它代表两个datetime之间的时间差。我们可以使用它来实现。

例子：

import datetime
now = datetime.datetime.now()
date = now + datetime.timedelta(days = 1)

现在date就是明天了。当然，如果想得到昨天，就减去1.

#秒减去1

date = now + datetime.timedelta(seconds = -1)
'''