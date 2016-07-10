import os
from random import randint
global a
global b
global counter
global user_input
global output
global line
user_input = 10
counter = 1
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))


def main(counter, user_input):


	def goto(linenum):
	    line = linenum


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
	line = 1
	while True:
	    if line == 1:
	    	output = ""
	        while counter < user_input:
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

		        entry_list = str(w)
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
	        	output = output + entry_list + "\n"
	    		counter += 1
	        line = 20
	        goto(20)
	    elif line == 20:
	        break
	return output


if __name__ == "__main__":
	main(counter, user_input)
