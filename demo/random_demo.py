import string
import random


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
choice(seq)	从序列的元素中随机挑选一个元素，比如random.choice(range(10))，从0到9中随机挑选一个整数。
randrange ([start,] stop [,step])	从指定范围内，按指定基数递增的集合中获取一个随机数，基数默认值为 1
random()	随机生成下一个实数，它在[0,1)范围内。
seed([x])	改变随机数生成器的种子seed。如果你不了解其原理，你不必特别去设定seed，Python会帮你选择seed。
shuffle(lst)	将序列的所有元素随机排序
uniform(x, y)	随机生成下一个实数，它在[x,y]范围内。
'''

print(random.choice(range(10)))
