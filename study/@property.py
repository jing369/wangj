#!/usr/bin/python
# -*- coding: UTF-8 -*
#在绑定属性时，如果我们直接把属性暴露出去，虽然写起来简单，但是没办法检查参数，导致可以把成绩随笔昂改
#s = Student()
#s.score = 9999

#为了显示score的范围，可以通过一个set_score()方法来设置成绩，在通过一个get_score()来获取成绩
'''
class Student(object):

    def get_score(self):
        _score = self._score

    def set_score(self,value):
        if not isinstance(value,int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0~100!')
        self._score = value

s = Student()
s.set_score(60)
s.get_score()
print s._score

s.set_score('aa')
s.get_score()
print s._score
'''


"""
class Student(object):

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self,value):
        if not isinstance(value,int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0~100!')
        self._score = value


s = Student()
s.score = 60  #ok，实际转化为s.set_score(60)
print 's.score=,'s.score  #ok,实际准化为s.get_score()
# ValueError: score must between 0 ~ 100!
s.score = 999
"""





# Python内置的@property装饰器就是负责把一个方法变成属性调用的

# @property广泛应用在类的定义中，可以让调用者写出简短的代码，同时保证对参数进行必要的检查，这样，程序运行时就减少了出错的可能性。

class Screen(object):
    @property
    def width(self):
        return self._width

    @width.setter
    def width(self,value):
        self._width = value

    @property
    def height(self):
        return self._heigh

    @height.setter
    def heigh(self, value):
        self._height = value

    @property
    def resolution(self):
        return self._width * self._height


s = Screen()
s.width = 1024
s.heigh = 768
print ('resolution =',s.resolution)
if s.resolution == 786432:
    print ('测试通过')
else:
    print ('测试失败')







