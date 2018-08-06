"""
*Задача-1*
Написать декоратор который будет выводить время выполнения вашей функции

*Задача-2*
Написать декоратор который будет расширять(добавлять) аргументы к вашей функции.

*Задача-3*
Написать декоратор который будет выполнять предпроверку типа аргумента который передается в вашу функцию.
 Если это int, тогда выполнить функцию и вывести результат, если это str(),
  тогда зарейзить ошибку ValueError (raise ValueError(“string type is not supported”))

*Задача-4*
Написать декоратор с аргументом. Принимает на вход ip_address.
 Декоратор будет обрабатывать ошибку которую вы рейзите в вашей функции.
 Записывать трейс ошибки в текстовый файл.
 Вывести сообщение “File {} sent to server {}“.format(file_name, decarator_args)

*Задача-5*
Написать КЛАСС декоратор tracer который будет считать количество вызова вашей функции и выводить его.

*Задача-6*
Написать функцию которая принимает целое число и преобразует его в римскую систему счета
```ROMANS = (('M', 1000),
              ('CM', 900),
              ('D', 500),
              ('CD', 400),
              ('C', 100),
              ('XC', 90),
              ('L', 50),
              ('XL', 40),
              ('X', 10),
              ('IX', 9),
              ('V', 5),
              ('IV', 4),
              ('I', 1))```

*Задача-7*
Дан массив целых чисел. Нужно найти сумму элементов с четными индексами и перемножить эту сумму
на последний элемент исходного массива.

*Задача-8*
Дан массив целых цисел, вернуть наименьшее целое число(больше 0) которого нет в исходном массиве.
  Например list = [1, 2, 3, 4] результат = 5

*Задача-9*
Необходимо зашифровать текст сообщения
(в исходных данных не будет специальных символов вроде “!”, “&”, “?”, только текст и пробелы)
 используя шифр где каждая буква исходного текста заменяется другой,
  которая находится на определенном расстоянии в алфавите. Например, (“a b c”, 3) == “d e f”

*Задача-10*
Отсортировать тапл по его элементу float
Пример data = [(‘data1’, ‘12,0’), (‘data2’, ‘9.1’), (‘data3’, ‘14.5’)]

*Задача-11*
Дан массив из таплов, необходимо убрать все пустые таплы из массива
list = [(), (), (‘’,), (‘a’, ‘b’), (‘a’, ‘b’, ‘c’), (‘d’)]
"""

#
# # PythonDecorators/entry_exit_function.py
# def entry_exit(f):
#     def new_f():
#         print("Entering", f.__name__)
#         f()
#         print("Exited", f.__name__)
#     return new_f
#
# @entry_exit
# def func1():
#     print("inside func1()")
#
# @entry_exit
# def func2():
#     print("inside func2()")
#
# func1()
# func2()
# print(func1.__name__)
#
#


# *Задача-1*
# Написать декоратор который будет выводить время выполнения вашей функции
import time


def check_time(f):
    def new_f():
        starttime = time.time()
        print("Start time:", starttime)
        f()
        endtime = time.time()
        print("End time:", endtime)
        print("RUN time:", endtime - starttime, "sec")
    return new_f


@check_time
def func_foo():
    print("Function!")
    time.sleep(1)
    print("End Of Function!")


func_foo()
###############################################

# *Задача-2*
# Написать декоратор который будет расширять(добавлять) аргументы к вашей функции.


def check_time_arg(*args):

    def check_time(f):
        print("CHECK_TIME_DECOR: List of args:", [arg for arg in args])

        def new_f(*args_f):
            starttime = time.time()
            print("Start time:", starttime)

            args_f_new = list(args_f)
            args_f_new.append("using_decorator")
            args_new_tuple = tuple(args_f_new)
            f(*args_new_tuple)
            #     args_new_tuple = tuple(list(args_f).append("using decorator2"))
            #     f(*args_new_tuple)
            # f(*tuple(list(args_f).append("using decorator2")))
            # f(*args_f)
            endtime = time.time()
            print("End time:", endtime)
            print("RUN time:", endtime - starttime, "sec")
        return new_f
    return check_time


@check_time_arg("DEC_ARG1", "DEC_ARG2", "DEC_ARG3", "DEC_ARG4")
def print_decor_args(*args):
    print("List of args:", [arg for arg in args])


print_decor_args("ARG1", "ARG2", "ARG3", "ARG4")
print_decor_args("new_ARG1", "new_ARG2", "new_ARG3", "new_ARG4")


# TASK #3
# Написать декоратор который будет выполнять предпроверку типа аргумента который передается в вашу функцию.
#  Если это int, тогда выполнить функцию и вывести результат, если это str(),
#  тогда зарейзить ошибку ValueError (raise ValueError(“string type is not supported”))


def check_type(f):

    def new_f(arg1):
        if isinstance (arg1 , int):
            print("INT:", arg1)
            f(arg1)
        else:
            print("NOT_INT !!!")
            raise ValueError("string type is not supported")
    return new_f


@check_type
def func_int(int_var):
    print("Function:", int_var**2)
    # print("INT:", int_var)
    return


func_int(3)
# UNcomment next line
# func_int('asd')
##############################################


# Task 4
# Написать декоратор с аргументом. Принимает на вход ip_address.
#  Декоратор будет обрабатывать ошибку которую вы рейзите в вашей функции.
#  Записывать трейс ошибки в текстовый файл.
#  Вывести сообщение “File {} sent to server {}“.format(file_name, decarator_args)
import traceback


def check_type(f):

    def new_f(arg1):
        try:
            f(arg1)
        except Exception as err:
            print("Decorator exception:", err)
            print(traceback.format_exc())
            # ValueError("string type is not supported")
    return new_f


@check_type
def func_int(int_var):
    if isinstance(int_var, int):
        print("INT:", int_var)
        print("Function:", int_var**2)
        print()
    else:
        print("NOT_INT !!!")
        # print("File {} sent to server {}".format(file_name, decorator_args))
        raise ValueError("string type is not supported")
    # print("INT:", int_var)
    return


func_int(3)
# uncomment next line
# func_int('asd')
######################################


# Task 5
# Написать КЛАСС декоратор tracer который будет считать количество вызова вашей функции и выводить его.


class count_call():

    def __init__(self, *arg1):
        """ If there are decorator arguments, the function
            to be decorated is not passed to the constructor! """
        print("Inside __init__()")
        self.arg1 = arg1
        self.counter = arg1[0]

    def __call__(self, f):
        """ If there are decorator arguments, __call__() is only called
                once, as part of the decoration process! You can only give
                it a single argument, which is the function object. """
        print("Inside __call__()")

        def wrapped_f(*args):
            print("Inside wrapped_f()")
            print("Decorator arguments:", self.arg1)
            f(*args)
            self.counter += 1
            print("After f(*args)")
            print("Call Nr:", self.counter)
            print()
        return wrapped_f


@count_call(500)
def func_for_count(*args):
    print("func_for_count   !!!")
    print("Function arguments:", args)


func_for_count()
func_for_count(1, 1, 1, 11)
func_for_count(2, 2, 2, 22)
func_for_count(3, 3, 3, 33)


# Task 7
# *Задача-6*
# Написать функцию которая принимает целое число и преобразует его в римскую систему счета
"""
ROMANS = (('M', 1000),
              ('CM', 900),
              ('D', 500),
              ('CD', 400),
              ('C', 100),
              ('XC', 90),
              ('L', 50),
              ('XL', 40),
              ('X', 10),
              ('IX', 9),
              ('V', 5),
              ('IV', 4),
              ('I', 1))
"""
'''1,4,5,9,10,40,50,90,100,400,500,900,1000'''

ROMANS = (('M', 1000),
              ('CM', 900),
              ('D', 500),
              ('CD', 400),
              ('C', 100),
              ('XC', 90),
              ('L', 50),
              ('XL', 40),
              ('X', 10),
              ('IX', 9),
              ('V', 5),
              ('IV', 4),
              ('I', 1))

'''
{'name': 'Dmitriy', 'city': 'Lviv', 'age': 21}]
'''
'''
sorted_by_age = sorted(data, key=lambda x: x['age']) # Sort by age
'''

base_list = sorted(list(ROMANS), key=lambda x: x[1], reverse=True)

# Input_year = input()
Input_year = "2018"
result = ''
for mnemonic in base_list:
    check = int(Input_year)//mnemonic[1]
    # print("For check:", check)
    # print("Mnemonic :", mnemonic)
    if check != 0:
        # print("If check:", check)
        result += check*mnemonic[0]
        # print("resultStr:", result)
        Input_year = int(Input_year) - check*mnemonic[1]
        # print("Input year:", Input_year)

print(base_list)
print(result)

# Task 8
# Дан массив целых цисел, вернуть наименьшее целое число(больше 0) которого нет в исходном массиве.
#   Например list = [1, 2, 3, 4] результат = 5


# Task 9
# Необходимо зашифровать текст сообщения
# (в исходных данных не будет специальных символов вроде “!”, “&”, “?”, только текст и пробелы)
#  используя шифр где каждая буква исходного текста заменяется другой,
#   которая находится на определенном расстоянии в алфавите. Например, (“a b c”, 3) == “d e f”

str = "aA bB cC zZ !@#a"
n = 3

for c in str:
    c_int = ord(c)
    if (c_int >= 65 and c_int <= 90):
        c_int_out = c_int + n
        if c_int_out > 90:
            c_int_out -= 26
    elif (c_int >= 97 and c_int <= 122):
        c_int_out = c_int + n
        if c_int_out > 122:
            c_int_out -= 26
    else:
         c_int_out = c_int
    print(chr(c_int_out), end="")
print()

"""
a - 97
A - 65
z - 122
Z - 90
"""

# Task 10
# Отсортировать тапл по его элементу float
# Пример data = [(‘data1’, ‘12,0’), (‘data2’, ‘9.1’), (‘data3’, ‘14.5’)]

data = [('data1', '12.0'), ('data2', '9.1'), ('data3', '14.5')]


data_sorted = sorted(data, key=lambda x : float(x[1]), reverse=True)
# data_sorted = sorted(data, key=lambda x : float(x[1]))
print("data_sorted:", data_sorted)


# Task 11
# Дан массив из таплов, необходимо убрать все пустые таплы из массива
# list = [(), (), (‘’,), (‘a’, ‘b’), (‘a’, ‘b’, ‘c’), (‘d’)]

list = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
list_out = []
for a in list:
    if a :
        list_out.append(a)
    else:
        print("None:", a)

print(list_out)

