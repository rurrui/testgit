import json


class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score


def stu2dict(stu):
    return {
        'name': stu.name,
        'age': stu.age,
        'score': stu.score
    }


s = Student('wzh', 23, 99)
print(json.dumps(s, default=stu2dict))
