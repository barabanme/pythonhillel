import doctest # Тесты находятся в описании функции
import itertools
#
# >>>assert [], 42
# Traceback (most recent call last):
#   File "<input>", line 1, in <module>
# AssertionError: 42
#
#
#
# ###
# message = "{} != {}".format(actual, result)
# assert actual == result, message
# ###
#
# import this
#
# assert False, "Text if first arg FALSE"
# assert True, "Text if first arg FALSE"
#
#
# использование Директив
#
# def rle(iterable):
#
#
#     pass


# import unittest
#
# class TestCases(unittest.TestCase): # все ТЕСТЫ должны начинаться со слова "test"
#     def test_rle(self):
#         # self.assertEqual(rle("mississippi"), [...])
#         print("test_rle")
#         pass
#
#     def setUp(self): #выполняется ПЕРЕД каждым тестом в этом классе
#         pass
#
#     def tearDown(self): #выполняется ПОСЛЕ каждого теста в этом классе
#         pass


from hypothesis import given
import hypothesis.strategies as st

@given(st.integers(), st.integers())
def test_ints_are_commutative(x, y):
    assert x + y == y + x

@given(x=st.integers(), y=st.integers())
def test_ints_cancel(x, y):
    assert (x + y) - y == x

@given(st.lists(st.integers()))
def test_reversing_twice_gives_same_list(xs):
    # This will generate lists of arbitrary length (usually between 0 and
    # 100 elements) whose elements are integers.
    ys = list(xs)
    ys.reverse()
    ys.reverse()
    assert xs == ys

@given(st.tuples(st.booleans(), st.text()))
def test_look_tuples_work_too(t):
    # A tuple is generated as the one you provided, with the corresponding
    # types in those positions.
    assert len(t) == 2
    assert isinstance(t[0], bool)
    assert isinstance(t[1], str)

# unittest in CI (Continues Integration)

# @given(lists(integers()))
# def test_sum_is_positive(xs):
#     assume(len(xs) > 10)
#     assume(all(x > 0 for x in xs))
#     print(xs)
#     assert sum(xs) > 0
