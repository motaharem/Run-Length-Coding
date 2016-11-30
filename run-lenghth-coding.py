import math
import os

def prefixcode(number):
    # A : prefix, fix length,codewordes for reminder
    for subdir,dirs,files in os.walk('./'):
        for file in files:
            if(file=='prefixcode.txt'):
                with open(subdir+file) as table:
                    number = int(number)
                    for line in table:
                        first_step =  line.split()
                        if (int(first_step[0])==number):
                            return first_step[1]
                return "-1"
    
def encode ():
    #read file && calculate m
    m = 0
    for subdir,dirs,files in os.walk('./'):
        for file in files:
            if (file == 'source.txt'):
                with open(subdir+file) as source:
                    count = 0
                    count0 = 0
                    count1 = 0
                    for word in source:
                        for ch in word:
                            count = count+1
                            if ch == '0':
                                count0 = count0 +1
                                #print ch,"^"
                            elif ch == '1':
                                count1 = count1 +1
                            else:
                                print "invalid character"
                                return
                    #print count,"__",count1,"__",count0
                    temp = float(count0)/float(count)
                    #print temp
                    m = round(-1 / math.log(temp, 2))
                    file1 = open(subdir+'m.txt', 'a')
                    file1.write(str(m))
                    
                file2 = open(subdir+'compress.txt', 'a')
                with open(subdir+file) as source:
                    for word in source:
                        count0 = 0
                        for ch in word:
                            if ch=='1':
                                q = count0 / m
                                for i in range(int(q)):
                                    file2.write('1')
                                file2.write('0')
                                code = prefixcode(count0 % m)
                                if (code != -1) :
                                    file2.write(code)
                                    #file.write("\n")
                                else:
                                    print "preix table error"
                                count0 = 0
                            if ch =='0':
                                count0 = count0 + 1 
                return

def decode ():
    #read file
    m = 0
    count1 = 0
    for subdir,dirs,files in os.walk('./'):
        for file in files:
            print "k",file
            if(file=='m.txt'):
                print "didesh"
                with open(subdir+'m.txt') as mfactor :
                    print 'ff'
                    for line in mfactor :
                        print "gg",line
                        x = line.split()
                        print x
                        m = int(float(x[0]))
            print "mm",m
        for file in files:
            if (file=='compress.txt'):
                with open(subdir+'compress.txt') as Input:
                    file1 = open(subdir+'decompress.txt', 'a')
                    while True:
                        char = Input.read(1)
                        if not char:
                            print ""
                            break
                        if (char=="1"):
                            count1 = count1 + 1
                        elif (char=="0"):
                            with open(subdir+'prefixcode.txt') as table:
                                R = 0
                                tag = True
                                Find = False
                                codeword = Input.read(6)
                                #print "codeword",codeword
                                for line in table:
                                    if(Find == False):
                                        first_step =  line.split()
                                        #print "line ",first_step," ",first_step[1],codeword
                                        if (first_step[1] == codeword):
                                            #print "YES"
                                            R = int(first_step[0])
                                            #print "R",first_step[0]
                                            number = count1*m + R
                                            #print "number",number
                                            #G = ""
                                            for k in range(number):
                                                #G = G+"0"
                                                file1.write("0")
                                            file1.write("1")
                                            #print G,"1\n"
                                            count1 = 0
                                            Find = True
                                            #print "_:",codeword, "number",number
                return

def check():
    for subdir,dir,files in os.walk('./'):
        for file in files:
            if(file=='source.txt'):
                with open(subdir+'source.txt') as S:
                    for subdir,dir,files in os.walk('./'):
                        for file in files:
                            if(file=='decompress.txt'):
                                with open(subdir+'decompress.txt') as D:
                                    while (True):
                                        s = S.read(1)
                                        d = D.read(1)
                                        if not s and not d:
                                            print "Yes :)"
                                            break
                                        if not s or not d :
                                            print "NO"
                                            break
                                        #if s == d :
                                        #print "Yes"

#main menu
print("Enter\n  1 if you want to encode\n  2 if you want to decode\n  3 to check equivalency of source and decompress\n")
func = raw_input()
if func == "1" :
    encode()
elif func == "2" :
    decode()
elif func == "3":
    check()
else:
    print "invalid input :|"
