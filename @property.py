# 如果直接设置一个类的属性，会因为缺少约束导致可以任意对属性赋值，所以我们需要对其进行约束，以下是两种方法
# 1.设置get_x(),set_x()方法
class Student(object):
    def get_score(self):
        return self.score
    def set_score(self,score):
        if not isinstance(score,int):
            print("score类型必须为int")
        elif score<0 or score>100:
            print("score超出范围")
        else:
            self.score=score
stu1=Student()
stu1.set_score('123')
stu1.set_score(1000)
stu1.set_score(99)
print(stu1.get_score())
# 2.使用@property
class Animal(object):
    @property
    def score(self):
        return self._score
    @score.setter
    def score(self,value):
        if not isinstance(value,int):
            print("score类型必须为int")
        elif value<0 or value>100:
            print("score超出范围")
        else:
            self._score=value
a=Animal()
a.score=99
print(a.score)
# practice
class Screen(object):
    @property
    def width(self):
        return self._width
    @width.setter
    def width(self,value):
        self._width=value
    @property
    def height(self):
        return self._height
    @height.setter
    def height(self,value):
        self._height=value
    @property
    def resolution(self):
        return self._width*self._height
s1=Screen()
s1.width=1024
s1.height=768
print(s1.resolution)