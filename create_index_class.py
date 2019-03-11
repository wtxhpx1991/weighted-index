
class Student(object):
    # 实例的变量名如果以__开头，就变成了一个私有变量（private）
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def print_score(self):
        print("%s's score is : %s" % (self.__name, self.__score))

    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError("bad score")


bart = Student("bart john", 123)
bart.get_score()
bart.print_score()
bart.set_score(10)


class Animal(object):
    def run(self):
        print("Animal is running")


class Dog(Animal):
    pass


class Cat(Animal):
    pass


dog = Dog()
dog.run()

type(bart)
type(dog)
dir(bart)
bart.__le__

# 想要限制实例的属性怎么办


class boy(object):
    __slots__ = ('name', 'age')


s = boy()
s.name = 'john'
s.age = 23
s.score = 33


# @property：将类中的一个方法变成属性调用

class Student1(object):
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError("bad input")
        if value < 0 or value > 100:
            raise ValueError("score must between 0 and 100")
        self._score = value


s = Student1()
s.score = 60
s.score = 9999

