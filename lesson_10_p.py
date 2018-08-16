class Counter():
    def __init__(self, counts=0):
        self.counts = counts

    def __call__(self, *args, **kwargs):
        self.counts += 1
        if self.counts >= 5:
            self.counts = 4
            print("WARNING OVERLOAD: counts SET to 4")

    def set_v(self, val):
        self.counts = val

    @property
    def get_v(self):
        return self.counts

    def view_v(self):
        print(self.counts)


class Child_1(Counter):

    def __init__(self):
        pass

    def add_attr(self):
        super().new_var = 1


class Child_2(Counter):

    def __init__(self):
        pass
        # print(self.__dir__(self))


def singleton(class_):
    instances = {}

    def getinstance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]
    return getinstance


@singleton
class MyClass(Counter):
    pass


m_class = MyClass()
m1_class = MyClass(22)

m1_class is m_class

m_class.view_v()
m1_class.view_v()


child1 = Child_1()

# child1.add_attr() # нельзя добавить аттрибут в родительский класс
child1.new_attribute = 4


import pprint

asd = child1.__dir__()
# pprint(asd)

child2 = Child_2()



temp = Counter()        # Создал объект класса

# temp.get_v()
temp.get_v
temp.set_v(23)
temp()
temp.get_v
temp.view_v()
print()


class Figure(object):
    def __init__(self):
        self.name = "line"
        self.a = 0
        pass


class Rect(Figure):
    def __init__(self, a=1, b=1):
        self.name = "Rect, a,b"
        self.a = a
        self.b = b

    def square(self):
        return self.a * self.b

    def perimeter(self):
        return 2*(self.a+self.b)


rect = Rect(5,6)
rect.perimeter()
rect.square()
rect.name