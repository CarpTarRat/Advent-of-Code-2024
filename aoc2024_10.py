def neighbourhours(position: tuple): #returns neighbours ordered from the right going anticlockwise
    if position == (0,0):
        return [(0,1),(1,0)]
    elif position == (39,0):
        return [(39,1),(38,0)]
    elif position == (39,39):
        return [(38,39),(39,38)]
    elif position == (0,39):
        return [(0,38),(1,39)]
    elif position[0] == 0:
        return [(0,position[1]+1),(0,position[1]-1),(1,position[1])]
    elif position[0] == 39:
        return [(39,position[1]+1),(38,position[1]),(39,position[1]-1)]
    elif position[1] == 0:
        return [(position[0],1),(position[0]+1,0),(position[0]-1,0)]
    elif position[1] == 39:
        return [(position[0]+1,39),(position[0],38),(position[0]-1,39)]
    else:
        return [(position[0]+1,position[1]),(position[0],position[1]+1),(position[0]-1,position[1]),(position[0],position[1]-1)]
    
def nghbs_no_prev(position: tuple, prev: tuple = None):
    nghbs = neighbourhours(position)
    if prev != None:
        nghbs.remove(prev)
        return nghbs
    else:
        return nghbs

def check_neighbours(nghb: list, height: int):
    for n,x in enumerate(nghb):
        if map[x[0]][x[1]] == height + 1:
            return n,x
    return False


map = []
with open('input10.txt') as input:
    for number,line in enumerate(input):
        line = line.replace('\n','')
        map.append([int(x) for x in list(line)])

trailheads = []
for number,row in enumerate(map):
    trailheads += [(number, column) for column in range(len(row)) if row[column] == 0]




trail_number = 0
scores = []
for i in range(len(trailheads)):
    nines = set()
    current_trail = []
    need_to_search = []
    position = trailheads[i]
    height = 0
    current_trail.append(position)
    nghb = nghbs_no_prev(position)
    next = check_neighbours(nghb, height)
    while True:
        if height == 9:
            nines.add(position)
            trail_number += 1
            position = current_trail[-2]
            height -= 1
            nghb = need_to_search[-1]
            next = check_neighbours(nghb, height)
            del current_trail[-1]
            del need_to_search[-1]
            continue
        if next == False:
            if len(current_trail) == 1:
                scores.append(len(nines))
                break
            else:
                position = current_trail[-2]
                height -= 1
                nghb = need_to_search[-1]
                next = check_neighbours(nghb, height)
                del current_trail[-1]
                del need_to_search[-1]
                continue
        else: 
            if next[0] == len(nghb) - 1:
                nghb = []
            else:
                nghb = nghb[next[0]+1:]
            need_to_search.append(nghb.copy())
            height += 1
            position = next[1]
            current_trail.append(position)
            print(current_trail, height, trail_number)
            nghb = nghbs_no_prev(position, current_trail[-2])
            next = check_neighbours(nghb, height)
print(trail_number)
print(sum(scores))
