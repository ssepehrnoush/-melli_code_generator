import os
import time
import generator__none_exe__
from random import randint
global a
global b
global loop5
global zero
global big_size
big_size = "how many you want in your file ?"
poop2 = ""
zero = 1


def goto(linenum):
    global line
    line = linenum


__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
input_txt = ("You can give it any numbers or type a name for getting"
             " a text file in your working directory")
loop = raw_input("How many do you need ?\n" + input_txt + "\n\n")


def quit():
    print("there is nothing to offer then")
    raise SystemExit


if loop == "0":
    quit()


def intlist(b):
    v = b
    ret = []
    while v != 0:
        v, m = divmod(v, 10)
        ret.insert(0, m)
    return ret


def read_text():
    triplets = open(os.path.join(__location__, 'source.txt'))
    contents_of_file = triplets.read()
    list1 = []
    i = contents_of_file[0]
    i = int(i)
    list1.append(i)
    for n in range(1, 2427):
        m = n + 1
        if(m % 4 != 0):
            a = contents_of_file[n]
            a = int(a)
            list1.append(a)
    return list1
    triplets.close()
all_valid_num = read_text()
list3_valid = []
p = 0
q = 3
for i in range(0, 607):
    list3_valid.append(all_valid_num[p:q])
    p += 3
    q += 3


def all():
    list_all = []
    x = 0
    y = 0
    z = 0
    for x in range(0, 10):
        for y in range(0, 10):
            for z in range(0, 10):
                    list_all.append([x, y, z])
    return list_all


list_all = all()
invalid_3 = [x for x in list_all if x not in list3_valid]


def multi():
    x = randint(34, 404)
    var = invalid_3[x]
    return var


def input_detect(input_txt):
    return input_txt.isdigit()


print "\n\n"
line = 1
while True:
    if line == 1:
        if loop == 0:
            goto(20)
            break
        x = multi()
        x0 = x[0]
        x1 = x[1]
        x2 = x[2]
        x = (x0 * 100) + (x1 * 10) + x2
        y = randint(0, 999999)
        z = 1000000*x + y
        n = 0
        summ = 0
        for n in range(0, 9):
            if n < 10:
                a = int(intlist(z)[n]) * (10 - n)
                summ = int(summ) + int(a)
                n += 1
        r = summ % 11
        e = [0, 1]
        if r in e:
            w = z*10 + r
        else:
            w = z*10 + 11 - r
        time.sleep(0.1)
        entry_list = str(w)
        if input_detect(loop) == True:
            poop = int(loop)
        else:
            alltogether = raw_input(big_size)
            while input_detect(alltogether) == False:
                alltogether = raw_input("type a number\n\n")
                line = 1
                goto(1)
            alltogether = int(alltogether)
            poop2 = loop + ".txt"
            goto(20)
            break
        x = 0
        for n in range(0, 9):
            if n < 10:
                a = int(entry_list[n]) * (10 - n)
                x = int(x) + int(a)
                n += 1
        r = x % 11
        y = [0, 1]
        if r in y:
            if r == int(entry_list[9]):
                c = "VALID"
        else:
            if int(entry_list[9]) == (11 - r):
                c = "VALID"
            else:
                c = "INVALID"
        print list(entry_list), ":", entry_list, "  ", c
        if zero < poop:
            zero += 1
            goto(1)
        else:
            goto(2)
    elif line == 2:
        print "               You are welcome"
        goto(20)
    elif line == 20:
        break


address = os.getcwd()
address = address + "\\" + poop2


def make_list(file_name):
    containts = generator__none_exe__.main(0, alltogether)
    file = open(file_name, "w")
    file.write(containts)
    file.close()
    print "Done"
    raise SystemExit


if poop2 != "":
    print address
    make_list(address)
