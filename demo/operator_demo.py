#算数运算符
# + - * / %(取余) **(幂) //(取整除-向下取接近商旳数)

a = 21
b = 10
c = 0
 
c = a + b
print ("1 - c 的值为：", c)
 
c = a - b
print ("2 - c 的值为：", c)
 
c = a * b
print ("3 - c 的值为：", c)
 
c = a / b
print ("4 - c 的值为：", c)
 
c = a % b
print ("5 - c 的值为：", c)
 
# 修改变量 a 、b 、c
a = 2
b = 3
c = a**b 
print ("6 - c 的值为：", c)
 
a = 10
b = 3
c = a//b 
print ("7 - c 的值为：", c)

print('---------------------------------------------')

#成员运算符
#   in  在指定的序列中找到值，返回True，否则返回False
#   not in  在指定的序列中找不到值，返回True，否则返回False
a = 10
b = 20
lists = [1, 2, 3, 4, 5 ]
 
if ( a in lists ):
   print ("1 - 变量 a 在给定的列表中 list 中")
else:
   print ("1 - 变量 a 不在给定的列表中 list 中")
 
if ( b not in lists ):
   print ("2 - 变量 b 不在给定的列表中 list 中")
else:
   print ("2 - 变量 b 在给定的列表中 list 中")
 
# 修改变量 a 的值
a = 2
if ( a in lists ):
   print ("3 - 变量 a 在给定的列表中 list 中")
else:
   print ("3 - 变量 a 不在给定的列表中 list 中")

print('---------------------------------------------')

#身份运算
#   is  判断两个标识符是否引用自一个对象
#   not is 判断两个标识符是否引用自不同对象

a = 20
b = 20
 
if ( a is b ):
   print ("1 - a 和 b 有相同的标识")
else:
   print ("1 - a 和 b 没有相同的标识")
 
if ( id(a) == id(b) ):
   print ("2 - a 和 b 有相同的标识")
else:
   print ("2 - a 和 b 没有相同的标识")
 
# 修改变量 b 的值
b = 30
if ( a is b ):
   print ("3 - a 和 b 有相同的标识")
else:
   print ("3 - a 和 b 没有相同的标识")
 
if ( a is not b ):
   print ("4 - a 和 b 没有相同的标识")
else:
   print ("4 - a 和 b 有相同的标识")

print('---------------------------------------------')

#is 与 == 区别：
#is 用于判断两个变量引用对象是否为同一个， == 用于判断引用变量的值是否相等。
a = [1,2,3,]
b = a
print(b)
print(id(a))
print(id(b))
print(bool(b is a))
print(bool(b == a))

b = a[:]
print(b)
print(id(a))
print(id(b))
print(bool(b is a))
print(bool(b == a))
