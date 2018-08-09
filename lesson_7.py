"""
Lesson 7
Work with strings, Files
__author__="aalex"
"""
import re


my_string = "here is string for  regexp"
law_courses = "Let reverence for the laws be breathed by every American mother " \
              "to the lisping babe that prattles on her lap. Let it be taught in " \
              "schools, in seminaries, and in colleges. Let it be written in primers, " \
              "spelling books, and in almanacs. Let it be preached from the pulpit," \
              " proclaimed in legislative halls, and enforced in the courts of justice." \
              " And, in short, let it become the political religion of the nation."

asd = re.compile("[^ ]+", re.I)

abc = asd.findall(my_string)
print(abc)

courses = asd.findall(law_courses)

print(courses)


list(map(ord, "hello"))

ooo = r"\N{DOMINO TILE HORIZONTAL-00-00}"

print(ooo.title().swapcase())

m_str = "foo bar"
m_str.ljust(16, '~')
print(m_str.ljust(16, '~'))
foo bar~~~~~~~~~
m_str.rjust(16, '~')
m_str.center(16, '~')

m_str.ljust(16)


m_str.lstrip("of")
m_str.rstrip("rb") # набор символов, НЕ СТРОКА!!!
m_str.strip()

m_str.split(" ")
m_str.partition(" ")
law_courses.partition(" ")
law_courses.startswith("le")
law_courses.find("mother")
law_courses.index("moth-er")
"""Traceback (most recent call last):
  File "<input>", line 1, in <module>
ValueError: substring not found"""

abracadabra = "abracadabra"
abracadabra.replace("ra", "**")

translate_map = {ord("a"): "+", ord("b"): "-"}
abracadabra.translate(translate_map)

"{}, {}, how are you?".format("Hello", "Sally", "asd")
"{}, {}, how are you?".format("Hello")

repr("я строка \t as")
repr(123)
'123'
str(1)
'1'
ascii("asdasdфівфів")

"{!s}".format("Ya Stroka-34-йцуйцуйцу")
#'Ya Stroka-34-йцуйцуйцу'
"{!r}".format("Ya Stroka-34-йцуйцуйцу")
# "'Ya Stroka-34-йцуйцуйцу'"
"{!a}".format("Ya Stroka-34-йцуйцуйцу")
# "'Ya Stroka-34-\\u0439\\u0446\\u0443\\u0439\\u0446\\u0443\\u0439\\u0446\\u0443'"
"{:~^70}".format("Ya Stroka-34-йцуйцуйцу") # like center
# '~~~~~~~~~~~~~~~~~~~~~~~~Ya Stroka-34-йцуйцуйцу~~~~~~~~~~~~~~~~~~~~~~~~'

"int: {0:d} hex {0:x} oct{0:o} bin(0:b)".format(42)
'int: 42 hex 2a oct52 bin(0:b)'

"{0}, {who}, {0}".format("hello", who="Kitty")

point = 0, 10
import string
string.whitespace
chunk = "я строка".encode("utf-8")
chunk.decode("cp1251")

import sys
sys.getdefaultencoding()

# open file modes (r,w,x,a,+,b,t)

asd = open("rrrrr.txt", "w+")
asd.write("asdasdasdas"
          "asdasdasdasd"
          "asdasdasdas"
          "asdasdas")
asd.fileno()
asd.write("qweqweqweqweqweqweqweqweqw")
aaaa = asd.readline()
asd.close()