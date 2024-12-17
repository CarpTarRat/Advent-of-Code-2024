import time
import numpy as np

lines = []
with open('input7.txt') as input:
    for line in input:
        line = line.replace('\n','').replace(':','')
        lines.append([int(x) for x in line.split(' ')])

possible = []
for n,line in enumerate(lines):
    print(n,len(possible))
    start = f'{0:0{len(line)-2}d}'
    while True:
        number = line[1]
        for i in range(len(start)):
            if start[i] == '0':
                number += line[2+i]
            elif start[i] == '1':
                number *= line[2+i]
        if number == line[0]:
            possible.append(line[0])
            break
        if start == '1' * (len(line)-2):
            break
        else:
            x = int(start,2) + 1
            start = f'{x:0{len(line)-2}b}'
print(len(possible))
print(sum(possible))

possible1 = []
for n,line in enumerate(lines):
    print(n,len(possible1))
    s = 0
    start = f'{int(np.base_repr(s,base=3)):0{len(line) - 2}d}'
    while True:
        number = line[1]
        for i in range(len(start)):
            if start[i] == '0':
                number += line[2+i]
            elif start[i] == '1':
                number *= line[2+i]
            elif start[i] == '2':
                number = int(str(number) + str(line[2+i]))
        if number == line[0]:
            possible1.append(line[0])
            break
        if start == '2' * (len(line)-2):
            break
        else:
            s += 1
            start = f'{int(np.base_repr(s,base=3)):0{len(line) - 2}d}'
print(len(possible1))
print(sum(possible1))

