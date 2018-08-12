class Student(object):
    def __init__(self,name):
        self.name=name
    def __str__(self):      # __str__可以把Student的实例格式化为正常字符串形式（以print输出时有效）
         return 'Student object (name: %s)' % self.name
    __repr__=__str__        #在py交互命令模式下，使以字符串形式输出
stu1=Student('wzh')
print(stu1)
# iter()
class Fob(object):
    def __init__(self):
        self.a,self.b=0,1
    def __iter__(self):
        return self
    def __next__(self):
        self.a,self.b=self.b,self.a+self.b
        if self.a>1000:
            raise StopIteration()
        return self.a
for n in Fob():
    print(n)
class Person(object):
    pass
dir(Person)
#  __getitem__()
class Fib(object):
  def __getitem__(self,n):
    # 当n是一个int数字时，Fib执行取指定索引操作
    if isinstance(n,int):
      a , b = 1, 1
      for x in range(n):
        a, b = b, a+b
      return a
        # 当n是一个slice时，Fib会做切片操作
    if isinstance(n,slice): 
      start=n.start
      stop=n.stop
      if start is None:
        start=0
        L=[]
        a,b=1,1
        for x in range(stop):
          if x>=start:
            L.append(a)
          a,b=b,a+b
        return a
f=Fib()
print(f[3])
# __call__
class Car(object):
    def __init__(self,name):
        self.name=name
    def __call__(self):
        print('My name is %s' % self.name)
c=Car('Benz')
c()