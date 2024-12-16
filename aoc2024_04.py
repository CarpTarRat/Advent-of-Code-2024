import regex

grid = []
with open('input4.txt') as input:
    for line in input:
        line = line.replace('\n','')
        grid.append(list(line))

rv_grid = list(reversed(grid))
number = 0
rows = [''.join(grid[i]) for i in range(len(grid))]
columns = [''.join([grid[j][i] for j in range(len(grid))]) for i in range(len(grid))]
diagonal_yx = [''.join([grid[i][j-i] for i in range(j + 1)]) for j in range(140)] + list(reversed([''.join([grid[-i-1][-j-1+i] for i in range(j + 1)]) for j in range(139)]))
diagonal_ymx = [''.join([rv_grid[i][j-i] for i in range(j + 1)]) for j in range(140)] + list(reversed([''.join([rv_grid[-i-1][-j-1+i] for i in range(j + 1)]) for j in range(139)]))
#for row in rows:
#    number += len(regex.findall('XMAS', row, overlapped = True))
#    number += len(regex.findall('XMAS', row[::-1], overlapped = True))
#for column in columns:
#    number += len(regex.findall('XMAS', column, overlapped = True))
#    number += len(regex.findall('XMAS', column[::-1], overlapped = True))
#for diagonal in diagonal_yx:
#    number += len(regex.findall('XMAS', diagonal, overlapped = True))
#    number += len(regex.findall('XMAS', diagonal[::-1], overlapped = True))
#for diagonal in diagonal_ymx:
#    number += len(regex.findall('XMAS', diagonal, overlapped = True))
#    number += len(regex.findall('XMAS', diagonal[::-1], overlapped = True))
#print(number)

s = regex.compile('MAS')
number = 0
loc = []
loc_yxr = []
loc_ymx = []
loc_ymxr = []
for j in range(len(diagonal_yx)):
    for i in s.finditer(diagonal_yx[j]):
        if j < 140:
            loc.append((i.start() + 1, j - (i.start() + 1)))
        else:
            loc.append((139 - i.start() - 1, j - 139 + i.start() + 1))

for j in range(len(diagonal_yx)):
    for i in s.finditer(diagonal_yx[j][::-1]):
        if j < 140:
            loc_yxr.append((j - (i.start() + 1), i.start() + 1))
        else:
            loc_yxr.append((j - 139 + i.start() + 1, 139 - i.start() - 1))

for j in range(len(diagonal_yx)):
    for i in s.finditer(diagonal_ymx[j]):
        if j < 140:
            loc_ymx.append((139 - i.start() - 1, j - (i.start() + 1)))
        else:
            pass
            loc_ymx.append((i.start() + 1, j - 139 + i.start() + 1))

for j in range(len(diagonal_yx)):
    for i in s.finditer(diagonal_ymx[j][::-1]):
        if j < 140:
            loc_ymxr.append((139 - j  + i.start() + 1, i.start() + 1))
        else:
            loc_ymxr.append((139 - (j - 139 + i.start() + 1), 139 - i.start() - 1))

for i in loc:
    if i in loc_ymx or i in loc_ymxr:
        number += 1
for i in loc_yxr:
    if i in loc_ymx or i in loc_ymxr:
        number += 1


print(number)

