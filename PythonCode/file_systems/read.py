'''
Modes:
r read 默认
w 以写入的方式打开文件，会覆盖原有的文件
a append if file exists 在已有文件中追加内容，不用重写
x 在新文件写入，文件已存在会报错
+ 表示可读写模式
文件的数据类型
t text   文本，默认
b binary 二进制
'''
stream = open('./demo.txt', '+rt', encoding='utf-8')
print(f'{str(stream.readable())}')
print(f'{stream.readline()}')
print(f'{stream.read(1)}')
print(f'{stream.readlines()}')
stream.close()
