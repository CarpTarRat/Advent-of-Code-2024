from collections import defaultdict
import numpy as np
from time import sleep

def add(a: tuple, b: tuple):
    return tuple(np.add(a,b))

def add_lr(a: tuple, b: tuple, lr: str):
    sum = tuple(np.add(a,b))
    return (sum[0], sum[1], lr)

def box_want(position: tuple, movement: tuple):
    want = add(position, movement)
    if want in walls:
        return False
    elif want in boxes:
        return box_want(want, movement)
    else:
        return want

def box_want_lr(position: tuple, movement: tuple, lr: set, to_check: list = [], number: int = None):
    lr1 = lr
    to_check1 = to_check
    want = add(position, movement)
    wantl = add_lr(position, movement, 'l')
    wantr = add_lr(position, movement, 'r')
    if wantl in testwallsd or wantr in testwallsd:
        return False
    elif wantl in testboxesd:
        lr1.add(wantl)
        right = (want[0],want[1]+1,'r')
        lr1.add(right)
        if movement == (0,1):
            return box_want_lr((right[0],right[1]), movement, lr1, to_check1)
        else:
            to_check1.append((want[0],want[1]+1))
            return box_want_lr(want, movement, lr1, to_check1)
    elif wantr in testboxesd:
        lr1.add(wantr)
        left = (want[0],want[1]-1,'l')
        lr1.add(left)
        if movement == (0,-1):
            return box_want_lr((left[0],left[1]), movement, lr1, to_check1)
        else:
            to_check1.append((want[0],want[1]-1))
            return box_want_lr(want, movement, lr1, to_check1)
    else:
        if to_check1 == []:
            return lr1
        else:
            wantf = to_check1[-1]
            del to_check1[-1]
            return box_want_lr(wantf, movement, lr1, to_check1)

def box_move_lr(boxesd: set, box_want: tuple, movement: tuple):
    for box in box_want:
        testboxesd.remove(box) #change back to boxesd after test done
    for box in box_want:
        testboxesd.add(add_lr((box[0],box[1]),movement,box[2]))
    return boxesd

def boxesd_positions():
    result = set()
    for box in testboxesd:
        result.add((box[0],box[1]))
    return result

def boxesd_positionsl():
    result = set()
    for box in testboxesd:
        if box[2] == 'l':
            result.add((box[0],box[1]))
    return result

def wallsd_positions():
    result = set()
    for wall in testwallsd:
        result.add((wall[0],wall[1]))
    return result

def show_map(position: tuple, size: int, movement: 'str'):
    boxes = boxesd_positions()
    walls = wallsd_positions()
    for i in range(2 *size + 1):
        for j in range(2 * size + 1):
            p1 = position[0] - size + i
            p2 = position[1] - size + j
            if (p1,p2,'l') in boxesd:
                print('L',end='')
            elif (p1,p2,'r') in boxesd:
                print('R',end='')
            elif (p1,p2) in walls:
                print('#', end='')
            elif (p1,p2) == position:
                print(movement,end='')
            else:
                print('.',end = '')
        print()

warehouse = []
moves = []
a= 0
with open('input15.txt') as input:
    for line in input:
        line = line.replace('\n','')
        if line == '':
            a =1
            continue
        if a == 0:
            warehouse.append(list(line))
        elif a == 1:
            moves += list(line)

walls = set()
boxes = set()
position = (0,0)

for number, row in enumerate(warehouse):
    for column, item in enumerate(row):
        if item == '#':
            walls.add((number, column))
        elif item =='O':
            boxes.add((number, column))
        elif item == '@':
            position = (number, column)

wallsd = set()
boxesd = set()
positiond = (0,0)
for number, row in enumerate(warehouse):
    for column, item in enumerate(row):
        if item == '#':
            wallsd.add((number, 2 * column, 'l'))
            wallsd.add((number, 2 * column+1, 'r'))
        elif item =='O':
            boxesd.add((number, 2*column, 'l'))
            boxesd.add((number, 2*column + 1, 'r'))
        elif item == '@':
            positiond = (number, 2*column)

while False:
    for number,move in enumerate(moves):
        print(number)
        if len(walls.intersection(boxes)) != 0:
            print(number)
            break
        if move == '<':
            want = add(position,(0,-1))
            if want in walls:
                continue
            elif want in boxes:
                boxwant = box_want(want, (0,-1))
                if boxwant == False:
                    continue
                else:
                    boxes.remove(want)
                    boxes.add(boxwant)
                    position = want
            else:
                position = want
        elif move == '^':
            want = add(position,(-1,0))
            if want in walls:
                continue
            elif want in boxes:
                boxwant = box_want(want, (-1,0))
                if boxwant == False:
                    continue
                else:
                    boxes.remove(want)
                    boxes.add(boxwant)
                    position = want
            else:
                position = want
        elif move == '>':
            want = add(position,(0,1))
            if want in walls:
                continue
            elif want in boxes:
                boxwant = box_want(want, (0,1))
                if boxwant == False:
                    continue
                else:
                    boxes.remove(want)
                    boxes.add(boxwant)
                    position = want
            else:
                position = want
        elif move == 'v':
            want = add(position,(1,0))
            if want in walls:
                continue
            elif want in boxes:
                boxwant = box_want(want, (1,0))
                if boxwant == False:
                    continue
                else:
                    boxes.remove(want)
                    boxes.add(boxwant)
                    position = want
            else:
                position = want

    sum = 0
    for number,box in enumerate(boxes):
        sum += box[0] * 100 + box[1]
    print(sum)
    print(position)
    print(sorted(list(boxes)))
    #print(walls.intersection(boxes))

testd = [list('##########'),
list('#..O..O.O#'),
list('#......O.#'),
list('#.OO..O.O#'),
list('#..O@..O.#'),
list('#O#..O...#'),
list('#O..O..O.#'),
list('#.OO.O.OO#'),
list('#....O...#'),
list('##########')]


testmoves = list('<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^' +
'vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v' +
'><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<' +
'<<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^' +
'^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><' +
'^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^' +
'>^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^' +
'<><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>' +
'^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>' +
'v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^')

testd = [list('#######'),
list('#...#.#'),
list('#.....#'),
list('#..OO@#'),
list('#..O..#'),
list('#.....#'),
list('#######'),]

testmoves = list('<vv<<^^<<^^')

testd = warehouse
testmoves = moves


testwallsd = set()
testboxesd = set()
testposition = (0,0)
for number, row in enumerate(testd):
    for column, item in enumerate(row):
        if item == '#':
            testwallsd.add((number, 2 * column, 'l'))
            testwallsd.add((number, 2 * column+1, 'r'))
        elif item =='O':
            testboxesd.add((number, 2*column, 'l'))
            testboxesd.add((number, 2*column + 1, 'r'))
        elif item == '@':
            testposition = (number, 2*column)

def test_map(move: 'str'):
    for i in range(len(testd)):
        for j in range(len(testd[0] * 2)):
            if (i,j,'l') in testboxesd:
                print('L',end='')
            elif (i,j,'r') in testboxesd:
                print('R',end='')
            elif (i,j,'l') in testwallsd or (i,j,'r') in testwallsd:
                print('#', end='')
            elif (i,j) == testposition:
                print(move,end='')
            else:
                print('.',end = '')
        print()


for number,move in enumerate(testmoves):
        if number > 700000:
            print()
            show_map(position, 10)
            print(number, position, move)
            print()
            break
        #print()
        #show_map(position, 10, move)
        #print(number, position, move)
        #print()
        #sleep(0.2)
        #test_map(move)
        print(number)
        sleep(0)
        #if len(wallsd_positions().intersection(boxesd_positions())) > 0:
        #    break
        if move == '<':
            boxwant = box_want_lr(testposition, (0,-1), to_check = [], lr = set())
            if boxwant == False:
                continue
            else:
                testboxesd = box_move_lr(testboxesd, boxwant, (0,-1))
                testposition = add(testposition, (0,-1))
        elif move == '^':
            boxwant = box_want_lr(testposition, (-1,0), to_check = [], lr = set())
            if boxwant == False:
                continue
            else:
                testboxesd = box_move_lr(testboxesd, boxwant, (-1,0))
                testposition = add(testposition, (-1,0))
        elif move == '>':
            boxwant = box_want_lr(testposition, (0,1), to_check = [], lr = set())
            if boxwant == False:
                continue
            else:
                testboxesd = box_move_lr(testboxesd, boxwant, (0,1))
                testposition = add(testposition, (0,1))
        elif move == 'v':
            boxwant = box_want_lr(testposition, (1,0), to_check = [], lr = set())
            if boxwant == False:
                continue
            else:
                testboxesd = box_move_lr(testboxesd, boxwant, (1,0))
                testposition = add(testposition, (1,0))

#print(sorted(list(boxesd)))
#sum = 0
#for number,box in enumerate(boxesd):
#    sum += box[0] * 100 + box[1]
#print(sum)
#print(position)
#print(len(a.intersection(boxesd)))
#print(here)
#print(walls.intersection(boxes))

sum = 0
boxesdl = boxesd_positionsl()
for number,box in enumerate(boxesdl):
        sum += box[0] * 100 + box[1]
print(sum)
