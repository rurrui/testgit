class Stuent(object):
    def __init__(self,name,score,gender):
        self.__name=name
        self.__score=score
        self.__gender=gender
    def print_score(self):
        print("%s:%s" % (self.__name,self.__score))
    def get_name(self):
        return self.__name
    def get_gender(self):
        return self.__gender
    def set_gender(self,gender):
        if gender!='Male':
            print("失败")
        else:
            self.__gender=gender
stu=Stuent("wzh",100,'Male')
stu.set_gender('middle')
gender1=stu.get_gender()
print("%s:%s" % (stu.get_name(),gender1))