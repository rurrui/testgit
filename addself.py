class Student(object):
    count=0
    def __init__(self,name):
        self.name=name
        Student.count+=1
wzh=Student('wzh')
rurui=Student('rurui')
print(Student.count)