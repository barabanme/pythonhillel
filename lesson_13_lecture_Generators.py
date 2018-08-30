# 27.08.2018
# Итераторы и генераторы


def iterator_func():
    return


def generator_func():
    return


# если объект определяет 2 магических метода __iter__, __next__
# - этот объект ИТЕРАТОР
#
# def __iter__():
#     return
#
# def __next__():
#     return

################################
# l = [1, 2, 3, 4, 5]
# it = iter(l)
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# # print(next(it))
from random import randint


def d6():
    return randint(1, 6)

for roll in iter(d6, 6):
    print(roll)

# функция next принимает итератор и вызывает у него метод __next__
# Можно также указать значение, которое возвращает
# в случае возникновения исключения StopIteration

next(iter([]), 42)


for elem in collection:
    do_something_here()

# метод in или not in используют магический метод __contains__

class seq_iter:
    def __init__(self, instance):
        self.instance = instance
        self.idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            res = self.instance[self.idx]
        except IndexError:
            raise StopIteration
        self.idx +=1
        return res


asd = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

aasd = seq_iter(asd)
next(aasd)
next(aasd)
next(aasd)
next(aasd)


############################
def my_func():
    print("Start")
    x=100
    print("X:", x)
    yield x
    x +=1
    yield x
    print("Done")
    return print("End of func")

gen = my_func()

next(gen)
##########################################


def unique(iterable, seen=None):
    seen = set(seen or [])
    for item in iterable:
        if item not in seen:
            seen.add(item)
            yield item


xs = [1,1,1,1,2,2,3,4,5,6]
unique(xs)
list(unique(xs))

# chain - объдинение 2-х map()


# пройти по генератору можно только 1 раз !!!!
def my_example():
    yield 100, 200


gen = my_example()
list(gen)
# >>>print(gen)
# <generator object my_example at 0x0437C2D0>
# >>>list(gen)
# [(100, 200)]


def my_example():
    yield 100


gen = my_example()
print(gen)
list(gen)
# >>>list(gen) # First time
# [100]
# >>>list(gen) # Second time
# []
########################################################
# ВЫРАЖЕНИЯ - ГЕНЕРАТОРЫ

gen = (elem for elem in range(10))
gen
next(gen)
list(gen)

#
#>>> gen = (elem for elem in range(10))
#>>> gen
# <generator object <genexpr> at 0x0437C300>
#>>> next(gen)
# 0
#>>> next(gen)
# 1
#>>> next(gen)
# 2
#>>> list(gen)
# [3, 4, 5, 6, 7, 8, 9]

# send при работе с генераторами

# ПОСМОТРЕТЬ ВИДЕО
# Девид Безле


def my_gen():
    res = yield
    print("Got {!r}".format(res))
    res = yield 100
    print("Got {!r}".format(res))

gen = my_gen()
next(gen)
next(gen)

#метод "send" возобнавляет выполнение генератора и передает значение в "yield"

gen = my_gen()
next(gen)
gen.send("Foobar")

def my_gen():
    try:
        res=yield
        print("Got {!r}".format(res))
        res=yield 100
        print("Got {!r}".format(res))
    except Exception as err:
        print(err)

gen.throw(ValueError, "Something wrong!")

##################
def my_ex():
    while True:
        try:
            yield 100
        finally:
            print("Done")

gen = my_ex()
next(gen)
gen.close()

#################################
# Сопрограмма
###############################

# def grep("Gotcha!"):


def grep(pattern):
    print("Looking for {!r}".format(pattern))
    while True:
        line = yield
        if pattern in line:
            print(line)

gen = grep("Gotcha!")
next(gen)
gen.send("asdasd asdasd adsdas Gotcha! asdfasdas")
gen.send("asdasd aGotcha! asdfasdas")
gen.send("asdasd aGocha! asdfasdas")

######################################

# Оператор yield from  позволяет делегировать выполнение другому генератору
def gen_range(first, last):
    for i in range(first, last):
        yield i

def gen_range1(first, last):
    yield from gen_range(0, 5)

asd = gen_range1(1,10)
next(asd)

#####################################

from itertools import islice
xs = range(10)
list(islice(xs, 3, 8, 2))
# [3,5,7]

from itertools import count
 for i in count(10):
     if



from itertools import cycle

count = 0
for item in cycle("XYZ"):
    if count > 7:
        break
    print(item)
    count +=1

from itertools import repeat

from itertools import dropwhile
list(dropwhile(lambda x: x<5, range(10)))
# [5, 6, 7, 8, 9]

from itertools import takewhile
list(takewhile(lambda x: x<5, range(10)))
# [0, 1, 2, 3, 4]

# chain - конкатенирует произвольное число итераторов

# list уникальных комбинаций из словаря "1234567890", по 2 элемента
from itertools import combinations
data = list(combinations("1234567890", 2))
print(data)
# print(data)
# [('1', '2'), ('1', '3'), ('1', '4'), ('1', '5'), ('1', '6'), ('1', '7'), ('1', '8'), ('1', '9'), ('1', '0'), ('2', '3'), ('2', '4'), ('2', '5'), ('2', '6'), ('2', '7'), ('2', '8'), ('2', '9'), ('2', '0'), ('3', '4'), ('3', '5'), ('3', '6'), ('3', '7'), ('3', '8'), ('3', '9'), ('3', '0'), ('4', '5'), ('4', '6'), ('4', '7'), ('4', '8'), ('4', '9'), ('4', '0'), ('5', '6'), ('5', '7'), ('5', '8'), ('5', '9'), ('5', '0'), ('6', '7'), ('6', '8'), ('6', '9'), ('6', '0'), ('7', '8'), ('7', '9'), ('7', '0'), ('8', '9'), ('8', '0'), ('9', '0')]
