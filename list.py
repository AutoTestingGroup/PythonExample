# -*- coding: utf-8 -*-
# Filename list.py Python list 常用操作

li = ["a", "b", "mpilgrim", "z", "example"]

print('**********  负数索引  **************')

print('输出倒数第一个元素')
print(li[-1])
print('输出倒数3个元素')
print(li[-3])
print('输出从第一个到倒数第一个元素')
print(li[1:-1])

print('**********  增加元素  **************')

print('增加一个对象,末位添加')
li.append('love')
print(li)
print('指定位置插入一个元素')
li.insert(2,'c')
print(li)

print('增加多个对象，末位添加')
li.extend(['xiaohua','MM'])
print(li)


print('**********  搜索  **************')
print('搜索love对应的索引')
print(li.index('love'))


print('**********  删除元素  **************')
print('删除指定元素')
li.remove('b')
print(li)
print('删除最后一个元素,并返回删除元素的值')
print(li.pop())


print('**********  运算符  **************')
print('通过运算的方式新增元素1')
li = li + ['hua', 'yang']
print(li)
print('通过运算的方式新增元素2')
li += ['two']
print(li)
print('通过运算的方式拷贝元素内容')
li = li * 2
print(li)


print('**********  使用join链接list成为字符串  **************')
# 字典
params = {"server":"mpilgrim", "database":"master", "uid":"sa", "pwd":"secret"}
# dict.items()  返回可遍历的(键, 值) 元组数组。
t = ["%s=%s" % (k, v) for k, v in params.items()]
print(t)
t = ";".join(["%s=%s" % (k, v) for k, v in params.items()])
print(t)