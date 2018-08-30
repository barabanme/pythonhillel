import itertools
import logging

# Formated Out
a = 2
asd = f"{a}"
print(asd)
###############################################################
var_1 = input("Var_1:")
var_2 = input("Var_2:")


def check_int(var):
    try:
        tmp = int(var)
        return True
    except ValueError:
        return False


if check_int(var_1) and check_int(var_2):
    print("Sum:", var_1 + var_2)
else:
    print("Conc:", var_1 + var_2)

#########################################################################
FORMAT = '%(asctime)-15s %(clientip)s %(user)-8s %(message)s'
logging.basicConfig(format=FORMAT)
d = {'clientip': '192.168.0.1', 'user': 'fbloggs'}
logger = logging.getLogger('tcpserver')


# logger.warning('Protocol problem: %s', 'connection reset', extra=d)


class FormatError(Exception):
    def check(self):
        pass

    def logerror(self, message):
        # logger.warning('LOG ERROR %s')
        print("Error Code:", message)
        pass


def some_func():
    raise FormatError
    pass


try:
    some_func()
except FormatError as err:
    err.logerror("123123123")

########################################################################################
list_1 = [i for i in range(10)]
list_2 = [i for i in range(11)]

for i, j in zip(list_1, list_2):
    print("i={}, j={}".format(i, j))
##################################################################

list(itertools.zip_longest(list_1, list_2))


class List_iter:
    def __init__(self):
        self.asd = [i for i in range(10)]
        self.idx = 0

    def __next__(self):
        try:
            res = self.asd[self.idx]
        except IndexError:
            raise StopIteration
        self.idx += 1
        return res

    def __iter__(self):
        try:
            res = self.asd[self.idx]
        except IndexError:

            raise StopIteration
        self.idx += 1
        return res


aasd = List_iter()

aasd.__iter__()
aasd.__next__()
######################################################################
class Logger(object):
    def __init__(self, val):
        self.val = val
        print("%d :: __init__" % self.val)

    def __enter__(self):
        print("%d :: __enter__" % self.val)

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("%d :: __exit__ " % self.val)
        if exc_type:
            print("%d !! error " % self.val)
            return True

for i in range(3):
    with Logger(i) as log:
        if i == 1:
            raise ValueError(i)

0 :: __init__
0 :: __enter__
0 :: __exit__
1 :: __init__
1 :: __enter__
1 :: __exit__
1 !! error
2 :: __init__
2 :: __enter__
2 :: __exit__


################################################
from contextlib import contextmanager


@contextmanager
def func():
    print(r"__init__")
    try:
        print(r"__enter__")
        yield
    except:
        print(r"__Exception__")
    finally:
        print(r"__exit__")

# func - MUST BE GENERATOR чтоб использовать @contextmanager()


with func() as f:
    print("Start FUNC()")

