# import this
# date = ('asd', 2013)
# dir(date)
# x = "foo" if True else print("qweqweqw")
# for i in range(100, 110, 1):
#     print(i)

#
# input_string = input()
# check=input_string[0]
# output_string=''
# for i in range(0,len(input_string)):
#     if i==0:
#         output_string += input_string[0]
#         # next()
#     else:
#         if input_string[i] == check:
#             print('input_string[i]:',input_string[i])
#             output_string +='$'
#         else:
#             output_string += input_string[i]
# print(output_string)
import re

def replace_ing():
    input_string = input()
    abc=''
    if len(input_string) < 3:
        print("output_string:",output_string)
        pass
    elif input_string.endswith("ing"):
        # abc = re.match("ing", "ly")
        output_string = re.sub("ing$", "ly", input_string)
    else:
        output_string = input_string+"ing"
    print(output_string)

def count_max():
    input_string = input()
    abc = input_string.split(" ")
    max_len = 0
    for words in abc:
        if len(words) > max_len:
            max_len=len(words)
    print(max_len)

def change_chars():
    input_string = input()

    first_char = input_string[0]
    last_char = input_string[-1]
    output_string = last_char + input_string[1:-1] + first_char

    print(output_string)

input_string = input()
output_string=''
if re.match('\[\[\]\]', input_string):
    output_string = re.sub(r"[[]]", "[[Python]]", input_string)
    print(output_string)
elif re.match('\{\{\}\}', input_string):
    output_string = re.sub(r"{{}}", "{{Java}}", input_string)
elif re.match('\<\<\>\>', input_string):
    output_string = re.sub(r"<<>>", "<<PHP>>", input_string)


# output_string = re.sub("\<\<\>\>", "<<PHP>>", input_string)
print(output_string)
left_list=(2,3,4,5,6,7,78,8,8,8,8,66,67,1222)
right_list = (3,4,5,6,4,343435345,5,4,3,4,5,4)
for i in left_list:
    if i in right_list:
        print(i)

#12
def ins_str_in_list():
    left_list=[2,3,4,5,6]
    ins_str = "asd"
    for i in range(0,len(left_list)):
        left_list[i]=ins_str+str(left_list[i])
    print(left_list)


# 13 SORT DICTIONARY BY VALUES

diction = {'banana':23, 'apple':12, 'cherry':18}
print(sorted(diction.items(), key=lambda x: x[1], reverse=True))

# 15
def sum_dict_val(diction):
    summ=0
    for i in diction:
        summ +=diction[i]
    print(summ)

# 16 MAP TWO LISTS INTO DICTIONARY
keys=['red','green','blue']
values=['#ff0000','#00ff00','#0000ff']

sum_dict={}
for i in range(0,len(keys)):
    # asd=keys[i]
    # print('asd:', asd)
    # aaa=values[i]
    sum_dict[keys[i]]=values[i]
print(sum_dict)

# 17 Remove duplicates from dict-dict

start_dict={
    "id1":{
        "name":"Sara",
        "class":"first",
        "subject":"subj1"
    }
}

