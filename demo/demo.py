import string
import random

'''
num = random.randint(0,100) #产生随机数，包含a和b   a<= num <= b
print(num)

A = string.ascii_letters    # 所有字母
# A = string.ascii_lowercase # 所有小写字母
# A = string.ascii_uppercase #所有的大写字母
b = random.choice(A)
#b = random.choices(A) #产生一个数组只有一个值
c = random.sample(A,3) #产生一个数组，有三个值
d = ""
i = 0
while i <= 3:
    d += random.choice(A)
    i +=1

print(A)
print(b)
print(c)
print(d)
'''

'''
#短路逻辑
#在Python中，None、任何数值类型中的0、空字符串“”、空元组()、空列表[]、空字典{}都被当作False，还有自定义类型，如果实现了 　__ nonzero __ ()　或　__ len __ () 方法且方法返回 0 或False，则其实例也被当作False，其他对象均为True。

print('空字符串布尔值为：', bool(''))
print('空列表布尔值为：',bool([]))
print('None布尔值为：',bool(None))
print('0布尔值为：',bool(0))
print('空元组布尔值为：',bool(()))
print('空字典布尔值为：',bool({}))
print('1布尔值为：',bool(1))

def test():
    return []

print(bool(test()))
print('--------------------')
'''
'''
def a():    #a() --> false
    print('A')
    return []

def b():    #b() --> false
    print('B')
    return[]

def c():    #c() --> true
    print('C')
    return 1

def d():    #a() --> false
    print('D')
    return []

def e():    #e() --> true
    print('E')
    return 1

def f():
    print('F')
    return 1

def g():
    print('G')
    return []

def h():
    print('H')
    return 1

if a() and b() and c() and d() and e(): #由于第一个函数返回的是false  and后面直接短路 if语句为true 所以不会打印end 
    print('end')    # 结果为A

print('-----------------')

if a() or b() or c() or d() or  e():    #or的左侧为false时不短路，所以会打印AB，or的左侧为true时，短路后面所有函数 if语句为true 所以打印end
    print('end')  #结果为 A B C end

print('-----------------')

if a() and b() and  c() and d() or e() and f() or g() and h():
    # and左侧为false 短路后面acd，遇到or继续执行 a()a or e()，执行e()，e()为true 所以接着直接执行 e()and f(),执行f(), f()为true，后面为or则短路后面所有函数。 
    print('end')    #结果为 AEF end
'''
'''
综上
从左至右运算，and左侧的逻辑值为False时，and后面全短路，直到遇到or，输出and左侧表达式到or右侧，参与接下来的运算
从左至右运算，or左侧的逻辑值为True时，or后面的表达式全部短路（不管是or还是and），直接输出or左侧表达式。
若 or 的左侧为 False ，或者 and 的左侧为 True 则不短路。
'''
'''
print('------------------------')
'''