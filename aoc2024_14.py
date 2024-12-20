import re

data = []
with open('input14.txt') as input:
    for line in input:
        pv = list(re.findall('[-0123456789]+', line))
        data.append([(int(pv[0]),int(pv[1])), (int(pv[2]),int(pv[3]))])

rows = 103
columns = 101
seconds = 100

final_positions = []
for pv in data:
    x_pos = pv[0][0] + seconds * pv[1][0]
    y_pos = pv[0][1] + seconds * pv[1][1]
    final_positions.append((x_pos % columns, y_pos % rows))

tl = 0
tr = 0
bl = 0
br = 0
for p in final_positions:
    if p[0] < 50 and p[1] < 51:
        tl += 1
    elif p[0] > 50 and p[1] < 51:
        tr += 1
    elif p[0] < 50 and p[1] > 51:
        bl += 1
    elif p[0] > 50 and p[1] > 51:
        br += 1
print(tl,tr,bl,br, tl*tr*bl*br)

t=0
positions = data.copy()
while True:
    for position in positions:
        position[0] = list(position[0])
        position[0][0] += position[1][0]
        position[0][0] = position[0][0] % columns
        position[0][1] += position[1][1]
        position[0][1] =position[0][1] % rows
        position[0] = tuple(position[0])
    t+=1
    print(t, len(set([p[0] for p in positions])), len(data))
    if len(set([p[0] for p in positions])) == 500:
        break