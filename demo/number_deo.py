import math
'''
数值类型
整型（int）
浮点型（float）
复数（complex）--> 由实部和虚部组成，z=a+bi，或者complex（a，b）表示，实部和虚部都是浮点型
'''

'''
数字常量
pi
e
'''

print(math.pi)
print(math.e)

'''
数字类型转换
int(x) --> 转换成整数
float(x) --> 转换成浮点数
complex(x) --> 转成复数，实部为X，虚部为0
complex(x,y) -->转成复数，实部为X，虚部为Y。
'''

'''
数学函数
abs(x)	返回数字的绝对值，如abs(-10) 返回 10
ceil(x)	返回数字的上入整数，如math.ceil(4.1) 返回 5
exp(x)	返回e的x次幂(ex),如math.exp(1) 返回2.718281828459045
fabs(x)	返回数字的绝对值，如math.fabs(-10) 返回10.0
floor(x)	返回数字的下舍整数，如math.floor(4.9)返回 4
log(x)	如math.log(math.e)返回1.0,math.log(100,10)返回2.0
log10(x)	返回以10为基数的x的对数，如math.log10(100)返回 2.0
max(x1, x2,...)	返回给定参数的最大值，参数可以为序列。
min(x1, x2,...)	返回给定参数的最小值，参数可以为序列。
modf(x)	返回x的整数部分与小数部分，两部分的数值符号与x相同，整数部分以浮点型表示。
pow(x, y)	x**y 运算后的值。
round(x [,n])	返回浮点数 x 的四舍五入值，如给出 n 值，则代表舍入到小数点后的位数。其实准确的说是保留值将保留到离上一位更近的一端。
sqrt(x)	返回数字x的平方根。
'''

a = -11.1

print(abs(a))
print(math.ceil(a))
print(math.exp(2))
print(math.fabs(a))
print(math.floor(a))
print(math.log(100,10))
print(math.pow(3,4))
print(math.sqrt(9))