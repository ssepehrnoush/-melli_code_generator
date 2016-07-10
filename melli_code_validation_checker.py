def goto(linenum):
    global line
    line = linenum

line = 1
while True:
    if line == 1:
        response = raw_input("Please enter your MELLI-CODE : ")
        if len(str(response)) == 10:
            goto(2)
        else:
            goto(3)
    elif line == 2:
        entry_list = list(response)
        print list(response)

        #n = 0
        x = 0
        for n in range(0, 9):
            if n < 10:
                a = int(entry_list[n]) * (10 - n)
                x = int(x) + int(a)
                n += 1
        #print "summury of the first 9 digits = ", x
        r = x % 11
        #print "R : summury % 11 =", r
        y = [0, 1]
        if r in y:
            #print " cuz its lower than 2 its must equal the last digit of the prime code . so it is : "
            if r == int(entry_list[9]):
                print "Valid"
        else:
            #print " cuz its bigger that 1 , the last digit of our code must equal ( 11-R ) so the code is :"
            if int(entry_list[9]) == (11 - r):
                print "Valid"
            else:
                print "Invalid"
        goto(20)
    elif line == 3:
        print "The entry code is invalid , please try again"
        goto(1)
    elif line == 20:
        break
    elif line == 100:
        print "You're annoying me - answer the question!"
        goto(1)

