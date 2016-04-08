#!/usr/bin/python
import sys

if len(sys.argv) != 2:
    print("usage: %s [arbiter br dbr xor rpa]+puf[2]"%(sys.argv[0]))
    exit(-1)
    
PufType = sys.argv[1]
try:
    fd = open(PufType + "\\finalAnalysisReport.txt","r")
    flog = open(sys.argv[1]+"_log.txt","w")
except IOError:
    print("Cannot open file %s"%(PufType))
    exit(-1)

for i in range(7):
    fd.readline()

NIST = {}
line = fd.readline()
while line:
    line = line.split()
    try:
        test = int(line[0])
    except:
        break
    name = line[-1]
    try:
        NIST[name]
    except KeyError:
        print("Now is %s"%(name))
        NIST[name] = []
    if line[-2]=='*':
        prop = line[-3]
    else:
        prop = line[-2]
    if prop[0]=='-':
        line = fd.readline()
        continue
    num = ''
    for i in range(len(prop)):
        if prop[i]=='/':
            break
        num+=prop[i]
    NIST[name].append(int(num))
    line = fd.readline()

for key,value in NIST.items():
    if not value:
        continue
    flog.write(key+':')
    mean = 0
    for i in range(len(value)):
        mean += value[i]
    mean /= len(value)
    flog.write(str(mean))
    flog.write('\n')
    
fd.close()
flog.close()