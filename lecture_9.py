"""
13.08.2018 Lesson_9
Lecture_5
Classes
"""
list_of_int = [i for i in range(2)]


class Counter:
    """ I count value """

    def __init__(self, initial=0):  # Constructor
        self.value = initial  # record attribute
        return

    def increment(self):  # Incrementer
        self.value += 1

    def get(self):  # Getter
        return self.value  # Read attribute


c = Counter(42)
c.increment()
c.get()
c.color = "fsdfsdf"  # Added new


# Перегрузка операторов

class Multiplyer(Counter):
    asd = "123"

    def eat(self):
        return self.asd


ml = Multiplyer()
print(ml.asd)
print(ml.value)


# Internal elements

class SomeClass:
    some_attr = 5
    _some_internal_attr = 10
    __some_very_internal_attribute = 15

SomeClass.some_attr
SomeClass._some_internal_attr
SomeClass.__some_very_internal_attribute
SomeClass._SomeClass__some_very_internal_attribute

# All classes nasleduyutsya from Class "Object"
sc = SomeClass()

sc.__doc__
sc.__name__
sc.__module__
sc.__bases__
sc.__class__
sc.__dict__

ml.__dict__

SomeClass.__dict__

vars(SomeClass)

# Ограничить добавление переменных в класс, так Класс занимает меньше места
class MyLimitedClass:
    __slots__ = ["name", "age", "country"]

limit = MyLimitedClass()
limit.age = 123
limit.color = 22
"""
>>>limit.age = 123
>>>limit.color = 22
Traceback (most recent call last):
  File "<input>", line 1, in <module>
AttributeError: 'MyLimitedClass' object has no attribute 'color'
>>>limit.color = 22
Traceback (most recent call last):
  File "<input>", line 1, in <module>
AttributeError: 'MyLimitedClass' object has no attribute 'color'
"""

# Обход ограничения на добавление аттрибутов Класса
class MyLimitedClassNew:
    __slots__ = ["name", "age", "country", "__dict__"]
    def __init__(self):
        self.birthday = 12
llm = MyLimitedClassNew()
llm.__slots__
llm.__dict__
"""
>>>llm.__dict__
{'birthday': 12}
>>>llm.__slots__
['name', 'age', 'country', '__dict__']
>>>llm.__dict__
{'birthday': 12}
"""

#@property
#Способ определения методов, вызываемыхх автоматически при обращении или присваивании аттрибутов Классу

class Attr:
    def __getattr__(self, name): #вызывается при добавлении аттрибута "age"
        if name == "age":
            return 100
        raise AttributeError

myClass = Attr()
myClass.age
myClass.ages

"""
>>>myClass = Attr()
>>>myClass.age
100
>>>myClass.ages
Traceback (most recent call last):
  File "<input>", line 1, in <module>
  File "<input>", line 5, in __getattr__
AttributeError
"""
####################################################################################
class MyClass:

    def __init__(self):
        self._age = 100

    @property
    def age(self):
        return 100

    @age.setter
    def age(self, new_age):
        return self._age

    @age.deleter
    def age(self):
        return


class Counter:
    def __init__(self, initial =0):
        self.value = initial


class OtherCounter(Counter):
    def get(self):
        return self.value


c = OtherCounter()
c.get()
c.value
#########################################################################################


class Counter:
    def __init__(self, initial =0):
        # self.__class__.all_counters.append(self)
        self.value = initial


class OtherCounter(Counter):
    def __init__(self, initial =0):
        self.initial = initial
        super().__init__(initial)

    def get(self):
        return self.value


oc = OtherCounter()
oc.__dict__
c.value

"""
>>>oc = OtherCounter()
>>>oc.__dict__
{'initial': 0, 'value': 0}
"""

##################################################


class A:
    def some_func(self):
        print("A.some_func()")


class B:
    def some_func(self):
        print("B.some_func()")


class C(A, B):
    pass

c = C()
c.some_func()
"""
Выполнит функцию из первого класса

>>>c = C()
>>>c.some_func()
A.some_func()
"""

###################################
#Method Resolution Order
#Use for MAIN CLASS (class definition)
C.__mro__
C.mro()
"""
>>>C.__mro__
(<class 'C'>, <class 'A'>, <class 'B'>, <class 'object'>)
>>>C.mro()
[<class 'C'>, <class 'A'>, <class 'B'>, <class 'object'>]
"""

##
# МИКСИН - Класс экземпляр которого не планирую создавать.
# они представляют методы, которые добавляются в прикладные классы наследованием


class Mixin(object):
    def __ne__(self, other):
        return not (self == other)


class Integet(Mixin):
    def __init__(self, i):
        self.i = i


#Декораторы Классов

import functools

def singltone(cls):
    instances={}
    @functools.wraps(cls)
    def wrapper(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return wrapper


## SINGLTONE - МОЖНО СОЗДАТЬ ТОЛЬКО 1 ЭКЗЕМПЛЯР КЛАССА
@singltone
class MyClass():
    """Do nothing"""

сс = MyClass()
сс1 = MyClass()

# Методы в классах:
# __setattr__ - вызывается в момент ИЗМЕНЕНИЯ какого либо аттрибута
# __getattr__ - вызывается в момент ЧТЕНИЯ какого либо аттрибута
##
##
setattr(my_class, "some_attribute", 100500)

#
# метод "__call__" вызывается если к классу обращаемся как к функции
#

class MyCall():

    def __call__(self, arg):
        print(arg)

    def __init__(self):
        self.arg = 0

mc = MyCall()
mc(123)
"""
>>>mc = MyCall()
>>>mc()
Traceback (most recent call last):
  File "<input>", line 1, in <module>
TypeError: __call__() missing 1 required positional argument: 'arg'
>>>mc(123)
123


"""