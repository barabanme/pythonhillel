# 25 July 2018, Wednesday

def function_test():
    pass


def decorate_func(func):
    def wrapper_around_orig_func():
        print("Start")
        func()
        print("End")
        return
    return wrapper_around_orig_func

# asd = decorate(function_test)
# asd

@decorate_func
def another_stand_alone_func():
    print("1")

#################################################################
def method_decorator(method_to_decorate):
    def wrapper(self, lie):
        lie = lie -3
        return method_to_decorate(self, lie)
    return wrapper

class Lucy(object):

    def __init__(self):
        self.age = 32

    @method_decorator
    def your_age(self, lie):
        print("I'm {} year old.".format(self.age + lie))

l=Lucy()
l.your_age(-3)
#################################################################

#######################################
def decorator_maker_with_arguments(decorator_arg1, decorator_arg2):
    print("I MAKE DECORATOR with decor_args:", decorator_arg1, decorator_arg2)

    def my_decorator(func):
        print("I'm DECORATOR, and You sent me decor_arguments:", decorator_arg1, decorator_arg2)

        def wrapper(function_arg1, function_arg2):
            print("I'm function around YOUr FUNCTION")
            return func(function_arg1, function_arg2)

        return wrapper

    return my_decorator

@decorator_maker_with_arguments("Vasya","Pupkin")
def func(arg1, arg2):
    print("Var in function:", arg1, arg2)


#######################################
from functools import partial

def add(x, y):
    return x+y

p_add = partial(add, 2)
p_add(4)

p2_add = partial(add, 6)
p2_add(6)
#####################################################

def decor(func):
    print("I'm decorator")
    print("Execute till start WRAPPER")
    def wrapper(*args):
        print("VARs to func:")
        return func(*args)
    return wrapper


def dec_vers(var_1, var_2):
    print("Init of decorator")
    print("var_1:", var_1)
    print("var_2:", var_2)
    def decor(func):
        print("I'm decorator")
        print("Execute till start WRAPPER")
        def wrapper(*args):
            print("VARs to func:", args)

            return func(*args)
        return wrapper
    return decor

@decor
def fff(*args):
    print("I'm FUNCTION in DECORATOR", args)

@dec_vers("VAR_1", "VAR_2")
def fff2(*args):
    print("I'm FUNCTION in DECORATOR", args)

fff(1, 2,3 ,4,55)
fff2(10,20,30)