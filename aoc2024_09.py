
map = ''
with open('input9.txt') as input:
    for number,line in enumerate(input):
        line = line.replace('\n','')
        map += line

blocks = []
filled_blocks = []
empty_blocks = []
f_blocks_pos = [] 
f_blocks_len = []
e_blocks_pos = []
e_blocks_len = []
filled = 0
empty = 0
for i in range(len(map)):
    x = int(map[i])
    if i % 2 == 0:
        length = len(blocks)
        filled_blocks += range(length, length + x)
        f_blocks_pos.append(length)
        f_blocks_len.append(x)
        blocks += [i // 2] * x
        filled += x
    elif i % 2 == 1:
        length = len(blocks)
        empty_blocks += range(length, length + x)
        e_blocks_pos.append(length)
        e_blocks_len.append(x)
        blocks += ['.'] * x
        empty += x
print(min(filled_blocks), max(filled_blocks), min(empty_blocks), max(empty_blocks))

min_empty = 0
while False:
    max_filled = max(filled_blocks)
    min_empty = min(empty_blocks)
    if min_empty > max_filled:
        break
    blocks[min_empty] = blocks[max_filled]
    blocks[max_filled] = '.'
    filled_blocks[filled_blocks.index(max_filled)] =  min_empty
    empty_blocks[empty_blocks.index(min_empty)] = max_filled
    print(min_empty,max_filled)

#checksum = 0
#for i in range(min_empty):
#    checksum += i * blocks[i]
#    print(checksum)
print(blocks[0:100])

for i in range(len(e_blocks_len)):
    if i > 0:
        del f_blocks_len[-1]
        del f_blocks_pos[-1]
    block_length = f_blocks_len[-1]
    block_pos = f_blocks_pos[-1]
    print(i,block_length, block_pos, e_blocks_len[0])
    for n,l in enumerate(e_blocks_len):
        if e_blocks_pos[n] >= block_pos:
            break
        if l >= block_length:
            blocks[e_blocks_pos[n]:e_blocks_pos[n] + f_blocks_len[-1]] = blocks[f_blocks_pos[-1]:f_blocks_pos[-1] + f_blocks_len[-1]]
            blocks[f_blocks_pos[-1]:f_blocks_pos[-1] +f_blocks_len[-1]] = ['.'] * f_blocks_len[-1]
            e_blocks_pos[n] += block_length
            e_blocks_len[n] -= block_length
            break
print(blocks[0:100])
checksum1 = 0
for i in range(len(blocks)):
    if blocks[i] != '.':
        checksum1 += i * blocks[i]
print(checksum1)