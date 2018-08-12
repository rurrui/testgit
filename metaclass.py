from Aloha import Aloha
a=Aloha()
a.aloha()
print(type(Aloha))
print(type(a))
# type()函数既可以返回一个对象的类型，又可以创建出新的类型，
# 比如，我们可以通过type()函数创建出Hello类，而无需通过class Hello(object)...的定义：
def fn(self,name='world'):
    print('Hello,%s.' % name)
Hello=type('Hello',(object,),dict(hello=fn))
h=Hello()
print(type(Hello))
print(type(h))
# metaclass
class ListMetaClass(type):
    def __new__(cls,name,bases,attrs):
        attrs['add']=lambda self,value:self.append(value)
        return type.__new__(cls,name,bases,attrs)
class MyList(list,metaclass=ListMetaClass):
    pass
l=MyList()
l.append(1)
print(l)