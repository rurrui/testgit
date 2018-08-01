class Student(object):
    def __init__(self,name,score):
        self.name=name
        self.score=score
    def print_score(self):
        print("%s:%s" % (self.name,self.score))
stu1=Student("wzh",99)
stu2=Student("rurui",98)
stu1.print_score()
stu2.print_score()