#!usr/bin/python
# -*- coding: utf-8 -*

class Student(object):
    pass

s = Student()
s.name = 'test'   #动态的给实例绑定一个属性
print ('动态的给实例绑定一个属性：'+s.name)

def set_age(self,age): #定义一个函数作为实例方法
    self.age = age

from types import MethodType
s.set_age = MethodType(set_age,s)  #给实例绑定一个方法
s.set_age(30)
print ('动态的给实例绑定一个方法：'+str(s.age))

# s2 = Student()
# s2.set_age(50)
# 为了给所有的实例都绑定方法，可以给class绑定方法,给class绑定方法后，所有实例均可调用
def set_score(self,score):
    self.score = score
Student.set_score = set_score

s.set_score(100)
print ('class绑定方法后，所有实例均可调用:' + str(s.score))



#为了达到限制的目的，Python允许在定义class的时候，定义一个特殊的__slots__变量，来限制该class实例能添加的属性
class People(object):
    __slots__ = ('name','age')

p = People()
p.name = 'wangjing'
p.age = 29
# p.score1 = 100  #由于score1没有被放到__slots__中，所以不能绑定score1属性
print ('限制实例绑定属性name：'+ p.name)
print ('限制实例绑定属性age：'+ str(p.age))

#使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的

class BlockPeople(People):
    pass
b = BlockPeople()
b.score1 = ('A')
print ('__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用:' + b.score1)