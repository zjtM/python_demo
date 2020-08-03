import configparser

#configparser --> 对配置文件进行增删改查
config = configparser.ConfigParser() #实例化
file = 'config.ini'
print(file)
config.read(file) #读取配置文件
'''
#config.add_section('login') #新增section 已经存在的section名  不能再次使用
config.set('login','username','333') #新增键值对,修改键值
config.set('login','password','555')
with open(file,'w') as configfile:
    config.write(configfile) #写入设置的section

print(file)
'''
username = config.get('login','username')#获取section的某个键的值
password = config.get('login','password')
print(username,password)

section = config.sections() #返回可用的section（主要是section名字）
print(section)
