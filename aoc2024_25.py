import numpy as np

with open('input25.txt') as input:
    locks = []
    keys = []
    data = [5,5,5,5,5]
    for n,line in enumerate(input):
        line = line.replace('\n','')
        if n % 8 == 0 and line == '.....':
            i = 1
            data = [5,5,5,5,5]
        elif n % 8 == 0 and line == '#####':
            i = 2
            data = [0,0,0,0,0]
        elif n % 8 == 7:
            if i == 1:
                keys.append(data.copy())
            elif i == 2:
                locks.append(data.copy())
        elif n % 8 == 6 and i == 1:
            continue
        else:
            if i == 1:
                for j in range(5):
                    if line[j] == '.':
                        data[j] -= 1
            elif i == 2:
                for j in range(5):
                    if line[j] == '#':
                        data[j] += 1
    locks.append(data)

locksn = [np.array(x) for x in locks]
keysn = [np.array(x) for x in keys]

def part_1():
    number = 0
    for lock in locksn:
        for key in keysn:
            fit = lock + key
            if np.all(fit <= np.array([5,5,5,5,5])):
                number += 1
    print(number)

if __name__ == "__main__":
    part_1()