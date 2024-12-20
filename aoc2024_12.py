from collections import defaultdict

farm = []
with open('input12.txt') as input:
    for number,line in enumerate(input):
        line = line.replace('\n','')
        farm.append(list(line))
print(len(farm), len(farm[0]))

def neighbourhours(position: tuple, size: int, vh: str = None): #returns neighbours ordered from the right going anticlockwise
    last = size - 1
    if position == (0,0):
        if vh == 'v':
            return [(1,0)]
        elif vh == 'h':
            return [(0,1)]
        return [(0,1),(1,0)]
    elif position == (last,0):
        if vh == 'v':
            return [(last-1,0)]
        elif vh == 'h':
            return [(last,1)]
        return [(last,1),(last-1,0)]
    elif position == (last,last):
        if vh == 'v':
            return [(last-1,last)]
        elif vh == 'h':
            return [(last,last-1)]
        return [(last-1,last),(last,last-1)]
    elif position == (0,last):
        if vh == 'v':
            return [(1,last)]
        elif vh == 'h':
            return [(0,last-1)]
        return [(0,last-1),(1,last)]
    elif position[0] == 0:
        if vh == 'v':
            return [(1,position[1])]
        elif vh == 'h':
            return [(0,position[1]+1),(0,position[1]-1)]
        return [(0,position[1]+1),(0,position[1]-1),(1,position[1])]
    elif position[0] == last:
        if vh == 'v':
            return [(last-1,position[1])]
        elif vh == 'h':
            return [(last,position[1]+1),(last,position[1]-1)]
        return [(last,position[1]+1),(last-1,position[1]),(last,position[1]-1)]
    elif position[1] == 0:
        if vh == 'v':
            return [(position[0]+1,0),(position[0]-1,0)]
        elif vh == 'h':
            return [(position[0],1)]
        return [(position[0],1),(position[0]+1,0),(position[0]-1,0)]
    elif position[1] == last:
        if vh == 'v':
            return [(position[0]+1,last),(position[0]-1,last)]
        elif vh == 'h':
            return [(position[0],last-1)]
        return [(position[0]+1,last),(position[0],last-1),(position[0]-1,last)]
    else:
        if vh == 'v':
            return [(position[0]+1,position[1]),(position[0]-1,position[1])]
        elif vh == 'h':
            return [(position[0],position[1]+1),(position[0],position[1]-1)]
        return [(position[0]+1,position[1]),(position[0],position[1]+1),(position[0]-1,position[1]),(position[0],position[1]-1)]
    
def check_neighbours(farmi: list,nghb: list, plant: str):
    number = 0
    for x in nghb:
        if farmi[x[0]][x[1]] == plant:
            number += 1
    return 4-number

def check_sides(current: tuple, farmi: list,nghb: list, plant: str):
    result = []
    for pos in nghb:
        if farmi[pos[0]][pos[1]] == plant:
            result.append(pos)
    number  = len(result)
    if number == 4:
        return 0
    elif number == 0:
        return 4
    elif number == 1:
        pos = result[0]
        if pos[0] == current[0]:
            count = len(good_neighbours(farmi,neighbourhours(pos,140, 'v'),plant))
        elif pos[1] == current[1]:
            count = len(good_neighbours(farmi,neighbourhours(pos,140, 'h'),plant))
        return 3 - number + count/2
    elif number == 2:
        pos1 = result[0]
        pos2 = result[1]
        difference_row = pos1[0] - pos2[0]
        difference_column = pos1[1] - pos2[1]
        if difference_row != 0 and difference_column != 0:
            current_diff_1_row = current[0] - pos1[0]
            current_diff_1_col = current[1] - pos1[1]
            if current_diff_1_row == 0:
                complete_square = set([(current[0] - difference_row, current[1] - current_diff_1_col)]) 
                count = len(set(good_neighbours(farmi,neighbourhours(pos1,140, 'v'),plant)).difference(complete_square)) + len(set(good_neighbours(farmi,neighbourhours(pos2,140, 'h'),plant)).difference(complete_square))
            else:
                complete_square = set([(current[0] - current_diff_1_row, current[1] - difference_column)])
                count = len(set(good_neighbours(farmi,neighbourhours(pos1,140, 'h'),plant)).difference(complete_square)) + len(set(good_neighbours(farmi,neighbourhours(pos2,140, 'v'),plant)).difference(complete_square))
            return 3 - number + count / 2
        else:
            if difference_row ==0:
                count = len(good_neighbours(farmi,neighbourhours(pos1,140, 'v'),plant)) + len(good_neighbours(farmi,neighbourhours(pos2,140, 'v'),plant))
            elif difference_column == 0:
                count = len(good_neighbours(farmi,neighbourhours(pos1,140, 'h'),plant)) + len(good_neighbours(farmi,neighbourhours(pos2,140, 'h'),plant))
            return count / 2
    elif number == 3:
        remaining = list(set(neighbourhours(current,140)).difference(set(result)))
        if len(remaining) == 0:
            return 0
        rem = remaining[0]
        difference_row = rem[0] - current[0]
        difference_column = rem[1] - current[1]
        if difference_row == 0:
            count = len(good_neighbours(farmi,neighbourhours(rem,140, 'v'),plant))
        elif difference_column == 0:
            count = len(good_neighbours(farmi,neighbourhours(rem,140, 'h'),plant))
        if count == 0:
            return 0
        elif count == 1:
            return 0.5
        elif count == 2:
            return 1

def good_neighbours(farmi: list, nghb: list, plant: str):
    result = []
    for pos in nghb:
        if farmi[pos[0]][pos[1]] == plant:
            result.append(pos)
    return result

farm2 = [list('RRRRIICCFF'), list('RRRRIICCCF'), list('VVRRRCCFFF'),list('VVRCCCJFFF'),list('VVVVCJJCFE'),list('VVIVCCJJEE'),list('VVIIICJJEE'),list('MIIIIIJJEE'),list('MIIISIJEEE'),list('MMMISSJEEE')]
plants = defaultdict(int)
for number, row in enumerate(farm):
    for column, plant in enumerate(row):
        if len(plant)> 1:
            continue
        position = (number, column)
        plants[plant] += 1
        to_visit = set(good_neighbours(farm, neighbourhours(position,140),plant))
        farm[position[0]][position[1]] = f'{farm[position[0]][position[1]]}{plants[plant]}'
        i=0
        while True:
            if len(to_visit) == 0:
                break
            position = list(to_visit)[0]
            to_visit.remove(position)
            to_visit = to_visit.union(set(good_neighbours(farm, neighbourhours(position,140),plant)))
            farm[position[0]][position[1]] = f'{farm[position[0]][position[1]]}{plants[plant]}'
            i+=1

size = 140
nghb_num = defaultdict(int)
sides = defaultdict(int)
plants2 = defaultdict(int)
for number,row in enumerate(farm):
    for column,plant in enumerate(row):
        #if plant != 'K1':
        #    continue
        plants2[plant] +=1
        nghb_num[plant] += check_neighbours(farm,neighbourhours((number,column),size),farm[number][column])
        sides[plant] += check_sides((number,column),farm,neighbourhours((number,column),size),farm[number][column])


price = 0
price1 = 0
for plant in plants2:
    price += plants2[plant] * nghb_num[plant]
    price1 += plants2[plant] * sides[plant]
print(sides)
print(plants2)
print(price)
print(price1)



