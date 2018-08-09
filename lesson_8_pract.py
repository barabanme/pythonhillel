"""
09.08.2018
pract after "Strings and HW 'logger'"
"""
#
# make file 5 lines? every line ends with "\n"
# remove all "\n" from file and rewrite file

#
f = open("test_file_lec8.txt", 'w')
f.write("hdjk hbakjdh bcjkash bdcbajksdh bcjkhbhbakjdh bcjkash bdcbajksdh bcjkhbhbakjdh bcjkash bdcbajksdh bcjkhbhbakjdh bcjkash bdcbajksdh bcjkhb \n")
f.write("hdjk hbakjdh bcjkash bdcbajksdh bcjkhbhbakjdh bcjkash bdcbajksdh bcjkhbhbakjdh bcjkash bdcbajksdh bcjkhbhbakjdh bcjkash bdcbajksdh bcjkhb \n")
f.write("hdjk hbakjdh bcjkash bdcbajksdh bcjkhbhbakjdh bcjkash bdcbajksdh bcjkhbhbakjdh bcjkash bdcbajksdh bcjkhbhbakjdh bcjkash bdcbajksdh bcjkhb \n")
f.write("hdjk hbakjdh bcjkash bdcbajksdh bcjkhbhbakjdh bcjkash bdcbajksdh bcjkhbhbakjdh bcjkash bdcbajksdh bcjkhbhbakjdh bcjkash bdcbajksdh bcjkhb \n")
f.write("hdjk hbakjdh bcjkash bdcbajksdh bcjkhb \n")
f.close()



#
# with open("test_file_lec8.txt", 'r') as f:
#     str_in_file = f.readlines()
#     str_in_file = "".join(str_in_file)
#     ssstr = re.sub(r"\n", "", str_in_file)
#     f.close()
#     with open("test_file_lec8.txt", 'w') as f:
#         f.write(ssstr)
#         f.close()

import re

with open("test_file_lec8_out.txt", 'w') as f_out:
    with open("test_file_lec8.txt", 'r') as f_in:
        str_in_file = f_in.readlines()
        for str_i in str_in_file:
            str_i = re.sub(r"[^ ]{5,}", "", str_i, 1)
            f_out.write(str_i)

f_out = open("test_file_lec8_out.txt", "r")
print(f_out.readlines())
f_out.close()


#######  3 ####################################

def read_data(filename="test_file_lec8.txt"):
    with open(filename, 'r') as ffile:
        f_in_list = ffile.readlines()
        return f_in_list


def write_data(f_out_list = None):
    with open("test_file_lec8_out2.txt", 'w') as ffile:
        ffile.writelines(f_out_list)
        return print("File writen")


in_list = read_data()
# max_len = [for i in in_list len(i)]
max_len = [len(tips) for tips in in_list]
max_len = max(max_len)
print(max_len)
out_list = []
for a in in_list:
    out_list.append(a.rjust(max_len, " "))

# print(out_list)
write_data(out_list)

#####################  4

f = open("test_file_lec8-nn.txt", 'w')
f.write("adjk a123-2341234\n")
f.write("kdjk k123-4523234\n")
f.write("adjk a234-0987234\n")
f.write("kdjk k234-4675234\n")
f.write("adjk a345-2567234\n")
f.write("hdjk 123422567234\n")
f.close()


in_list = read_data("test_file_lec8-nn.txt")
lists = [lll.split(" ") for lll in in_list]
asd = [item[1] for item in lists if re.match(r"^[ak]", item[0])]
print(asd)