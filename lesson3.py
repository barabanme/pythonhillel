# Functions in Python

def my_func():
    """
    Description of Function


    :return:
    """
    return print(100)

other_name = my_func
other_name()

def func():
    pass

func()
func.attr=100

print(dir(func()))
func.__dir__()

def my_func(a):
    def nested_func(x):
        return x**a
    return nested_func # return link to function
f=my_func(2) # Initialization of a
f(3) # 9
f(4) # 16

def my_func(a):
    nested_func=lambda n: n ** a
    return nested_func
f= my_func(2)
f(2)
f(3)
asd=float("-inf")

def fff(a, *args, **kwargs):
    print(a,args,kwargs)

fff(1,2,3, x=5,y=7)
"""
a=1
args=(2,3)
kwargs={'x':5, 'y':7}
"""

#############################################
# Change function depends on <TEST>
if <test>:
    action, args = func_1, (1,)
else:
    action, args = func_2, (1,2,3,4,5)
# call function
action(*args)
#############################################

*_, (first, *rest)=[range(1,5)]*5


##########################################
# recursive function

my_list =[1,[2,3,4],[5,6]]
def my_list_sum(my_list):
    total=0
    for elem in my_list:
        if isinstance(elem, list):
            total += my_list_sum(elem)
        else:
            total += elem
    return total
##########################################


