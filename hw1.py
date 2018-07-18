"""
Home Work

1) Сгенерировать dict() из списка ключей ниже по формуле (key : key* key).
keys = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
ожидаемый результат: {1: 1, 2: 4, 3: 9 …}

2) Сгенерировать массив(list()). Из диапазона чисел от 0 до 100 записать в результирующий массив только четные числа.

3) Заменить в произвольной строке согласные буквы на гласные.

4) Дан массив чисел.
[10, 11, 2, 3, 5, 8, 23, 11, 2, 5, 76, 43, 2, 32, 76, 3, 10, 0, 1]

4.1) убрать из него повторяющиеся элементы
4.2) вывести 3 наибольших числа из исходного массива
4.3) вывести индекс минимального элемента массива
4.4) вывести исходный массив в обратном порядке

5) Найти общие ключи в двух словарях:
dict_one = { ‘a’: 1,
                    ‘b’: 2,
                    ‘c’: 3,
                    ‘d’: 4 }

dict_two = { ‘a’: 6,
                    ‘b’: 7,
                    ‘z’: 20,
                    ‘x’: 40 }

6) Дан массив из словарей
data = [ {‘name’: ‘Viktor’, ‘city’: ‘Kiev’, ‘age’: 30 },
             {‘name’: ‘Maksim’, ‘city’: ‘Dnepr’, ‘age’: 20},
             {‘name’: ‘Vladimir’, ‘city’: ‘Lviv’, ‘age’: 32},
             {‘name’: ‘Andrey’, ‘city’: ‘Kiev’, ‘age’: 34},
             {‘name’: ‘Artem’, ‘city’: ‘Dnepr’, ‘age’: 50},
             {‘name’: ‘Dmitriy’, ‘city’: ‘Lviv’, ‘age’: 21}]

6.1) отсортировать массив из словарей по значению ключа ‘age'
6.2) сгруппировать данные по значению ключа 'city'
       вывод должен быть такого вида :
       {
          ‘Kiev’: [ {‘name’: ‘Viktor’, ‘age’: 30 },
                       {‘name’: ‘Andrey’, ‘age’: 34}],
          ‘Dnepr’: [ {‘name’: ‘Maksim’, ‘age’: 20 },
                          {‘name’: ‘Artem’, ‘age’: 50}],
          ‘Lviv’: [ {‘name’: ‘Vladimir’, ‘age’: 32 },
                       {‘name’: ‘Dmitriy’, ‘age’: 21}]
       }

"""


# 1.
print("1 Task:")
keys = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def dict_gen(keys):
    out_dict={}
    for i in keys:
        out_dict[i] = i*i
    return out_dict
print("dict_gen(keys):", dict_gen(keys))

# 2.
print()
print("2 Task:")
def gen_list():
    out_list=[]
    for i in range(2,101,2):
        out_list.append(i)
    return out_list
print("gen_list():", gen_list())





# 3.
print()
print("3 Task:")
vowels = ["A", "E", "I", "O", "U"]
consonants = ["B", "C", "D", "F", "G", "H", "J", "K", "L", "M", "N", "P", "Q", "R", "S", "T", "V", "W", "X", "Y", "Z"]

import random
in_str = input("INPUT STRING(A-Z):")
print("in_str:", in_str)

def vowels_func(in_str):
    out_str=""
    for i in range(0,len(in_str)):
        if in_str[i] in vowels:
            out_str += random.choice(consonants)
        else:
            out_str += in_str[i]
    return out_str

print("vowels_func(in_str):", vowels_func(in_str))

# 4.
print()
print("4 Task:")

in_array = [10, 11, 2, 3, 5, 8, 23, 11, 2, 5, 76, 43, 2, 32, 76, 3, 10, 0, 1]

# 4.1) убрать из него повторяющиеся элементы
# 4.2) вывести 3 наибольших числа из исходного массива
# 4.3) вывести индекс минимального элемента массива
# 4.4) вывести исходный массив в обратном порядке

wor_elements = set(in_array)
print("wor_elements w/o repeated elements:", wor_elements) # w/o repeated elements
print("3 MAX elements:",sorted(in_array, reverse=True)[:3]) # 3 MAX elements
print("index of min element in array:", in_array.index(min(in_array))) # index of min element in array
print("print array in reverse order", in_array[::-1]) # print array in reverse order


# 5. Найти общие ключи в двух словарях:
print()
print("5 Task:")

dict_one = { 'a': 1,
             'b': 2,
             'c': 3,
             'd': 4 }

dict_two = { 'a': 6,
             'b': 7,
             'z': 20,
             'x': 40 }

for keyA in dict_one:
    if keyA in dict_two:
        print("Common key:", keyA)

# 6. Дан массив из словарей
print()
print("6 Task:")

data = [ {'name': 'Viktor', 'city': 'Kiev', 'age': 30 },
         {'name': 'Maksim', 'city': 'Dnepr', 'age': 20},
         {'name': 'Vladimir', 'city': 'Lviv', 'age': 32},
         {'name': 'Andrey', 'city': 'Kiev', 'age': 34},
         {'name': 'Artem', 'city': 'Dnepr', 'age': 50},
         {'name': 'Dmitriy', 'city': 'Lviv', 'age': 21}]

# 6.1) отсортировать массив из словарей по значению ключа ‘age'
# 6.2) сгруппировать данные по значению ключа 'city'

sorted_by_age = sorted(data, key=lambda x: x['age']) # Sort by age
print(sorted_by_age)
#asd = sorted(data, key=lambda x: x['city']) # Sort by age

result_dict={}
for rec in data:
    getter = rec.get('city')
    if getter not in result_dict:
        result_dict[getter]=[]

    temp_fields={}
    for fields in rec:
        if fields != 'city':
            temp_fields[fields]=rec[fields]

    result_dict[getter].append(temp_fields)

print(result_dict)



