from time import sleep
import copy

with open('input6.txt') as input:
    lab = []
    for number, line in enumerate(input):
        line = line.replace('\n','')
        lab.append(list(line))
        if '>' in line:
            current_row = number
            current_column = line.index('>')
            current_state = '>'
        elif '<' in line:
            current_row = number
            current_column = line.index('<')
            current_state = '<'
        elif 'v' in line:
            current_row = number
            current_column = line.index('v')
            current_state = 'v'
        elif '^' in line:
            current_row = number
            current_column = line.index('^')
            current_state = '^'
 
print(len(lab), len(lab[0]), current_row, current_column, current_state)

initial_state = current_state
initial_row = current_row
initial_column = current_column

def hit_obstacle(current_state):
    if current_state == '^':
        return '>'
    elif current_state == '>':
        return 'v'
    elif current_state == 'v':
        return '<'
    elif current_state == '<':
        return '^'
    
def next_position(current_state, current_row, current_column):
    if current_state == '^':
        return (current_row - 1, current_column)
    elif current_state == '>':
        return (current_row, current_column + 1)
    elif current_state == 'v':
        return (current_row + 1, current_column)
    elif current_state == '<':
        return (current_row, current_column - 1)


positions = set()
while False:
    positions.add((current_row, current_column))
    next = next_position(current_state, current_row, current_column)
    print(next)
    if next[0] < 0 or next[0] >= 130 or next[1] < 0 or next[1] >= 130:
        break
    elif lab[next[0]][next[1]] == '#':
        current_state = hit_obstacle(current_state)
    else:
        current_row = next[0]
        current_column = next[1]
    #sleep(0.1)
print(len(positions))

obstacle_position = set()
for i in range(130):
    for j in range(130):
        if (i,j) == (initial_row, initial_column):
            continue
        print(i,j)
        lab_new = copy.deepcopy(lab)
        lab_new[i][j] = '#'
        current_state = initial_state
        current_row = initial_row
        current_column = initial_column
        states = set()
        while True:
            if (current_row, current_column, current_state) in states:
                obstacle_position.add((i,j))
                break
            else:
                states.add((current_row, current_column, current_state))
            next = next_position(current_state, current_row, current_column)
            if next[0] < 0 or next[0] >= 130 or next[1] < 0 or next[1] >= 130:
                break
            elif lab_new[next[0]][next[1]] == '#':
                current_state = hit_obstacle(current_state)
            else:
                current_row = next[0]
                current_column = next[1]
print(len(obstacle_position))
