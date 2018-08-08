class Student(object):
    pass
stu=Student()
stu.name='wzh' # 动态语言的特点，可以在创建实例后给实例绑定一个属性
print(stu.name)
# 给实例绑定一个方法
# 定义set_age为实例的方法
def set_age(self,age):
    self.age=age
from types import MethodType
stu.set_age=MethodType(set_age,stu) #给实例绑定一个set_age方法
stu.set_age(23)
print(stu.age)
# 以上的方法只是绑定到了stu实例上，并未为Student类创建一个set_age方法
#stu2=Student()
#stu2.set_age(23) # 报错
# 直接给class绑定一个方法
def set_score(self,score):
    self.score=score
Student.set_score=set_score
stu.set_score(99)
#stu2.set_score(98)
print(stu.score)
#print(stu2.score)


# 使用__slots__
class Animal(object):
    __slots__=('name','age') #__slots__规定Animal实例只能创建属性name和age，如下gender属性是不能设置的
a=Animal()
a.name='tom'
a.age=1
a.gender=0 #不能设置gender属性
# slots只对当前类有效，对继承子类无效
