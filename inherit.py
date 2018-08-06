import types
class Animal(object):
    def run(self):
        print('Animal is running')
class Dog(Animal):
    def run(self):
        print('Dog is running')
    def eat(self):
        print('Eat meat')
class Cat(Animal):
    def run(self):
        print('Cat is running')
dog=Dog()
cat=Cat()
dog.run()
cat.run()
print(isinstance(dog,Dog))
print(isinstance(cat,Cat))
print(type(dog))
print(type(cat))
print(type(abs))
print(type(abs)==types.BuiltinFunctionType)
print(type(lambda x:x)==types.LambdaType)
print(dir(dog))
class MyObject(object):
    def __init__(self):
        self.x=9
    def power(self):
        return self.x * self.x
obj=MyObject()
print(hasattr(obj,'x'))
print(getattr(obj,'x'))
setattr(obj,'y',19)
print(getattr(obj,'y'))