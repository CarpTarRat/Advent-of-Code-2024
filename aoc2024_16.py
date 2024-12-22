import numpy as np
from collections import defaultdict
from time import sleep

test1 = ['###############',
'#.......#....E#',
'#.#.###.#.###.#',
'#.....#.#...#.#',
'#.###.#####.#.#',
'#.#.#.......#.#',
'#.#.#####.###.#',
'#...........#.#',
'###.#.#####.#.#',
'#...#.....#.#.#',
'#.#.#.###.#.#.#',
'#.....#...#.#.#',
'#.###.#.#.#.#.#',
'#S..#.....#...#',
'###############']

test2 = ['#################',
'#...#...#...#..E#',
'#.#.#.#.#.#.#.#.#',
'#.#.#.#...#...#.#',
'#.#.#.#.###.#.#.#',
'#...#.#.#.....#.#',
'#.#.#.#.#.#####.#',
'#.#...#.#.#.....#',
'#.#.#####.#.###.#',
'#.#.#.......#...#',
'#.#.###.#####.###',
'#.#.#...#.....#.#',
'#.#.#.#####.###.#',
'#.#.#.........#.#',
'#.#.#.#########.#',
'#S#.............#',
'#################']

test3 = ['####################################################',
'#......................................#..........E#',
'#......................................#...........#',
'#....................#.................#...........#',
'#....................#.................#...........#',
'#....................#.................#...........#',
'#....................#.................#...........#',
'#....................#.................#...........#',
'#....................#.................#...........#',
'#....................#.................#...........#',
'#....................#.................#...........#',
'#....................#.............................#',
'#S...................#.............................#',
'####################################################']

test = []
with open('input16.txt') as input:
    for line in input:
        line = line.replace('\n','')
        test.append(line)

def add(a: tuple, b: tuple):
    return tuple(np.add(a,b))

def convert(test: list):
    walls = set()
    position = (0,0)
    exit = (0,0)
    for number, row in enumerate(test):
        #row = list(row)
        for column, item in enumerate(row):
            if item == "#":
                walls.add((number, column))
            elif item == 'E':
                exit = (number, column)
            elif item == 'S':
                position = (number,column)
    return walls, position, exit, len(test), len(test[0])

class MazeSolver:
    def __init__(self, walls: set, initial: tuple, exit: tuple, height: int, width: int):
        self.position = initial
        self.orient = (0,1)
        self.walls = walls
        self.exit = exit
        self.width = width
        self.height = height
        self.orientations = [(0,1),(-1,0),(0,-1),(1,0)]
        self.orient_pic = {(0,1): '>', (-1,0): '^', (0,-1): '<', (1,0): 'v'}
        self.history = [initial]
        self.orient_history = [(0,1)]
        self.tosearch = []
        self.solutions = []
        self.no_solutions = set()
        self.best_scores = defaultdict(int)
        self.best_score = 10000000000#130536 #11048 #7036  #run with >= in comment section below to get best score, then change > for part 2
        self.score = 0


    def search(self):
        dic =  {}
        for orientation in self.orientations:
            check = add(self.position, orientation)
            if check in self.walls or check in self.history:
                continue
            elif (check, orientation) in self.no_solutions:
                continue
            else:
                dic[orientation] = check 
        return dic
    
    def move_step(self, i: int = 0):
        possible = self.search()
        if self.orient in possible:
            self.position = possible[self.orient]
            del possible[self.orient]
            if len(possible) != 0 :
                for key in possible:
                    self.tosearch.append((len(self.history), {key: possible[key]}))
            self.update_history(i)
        elif len(possible) == 0:
            next = self.next_path(i)
            if next == False:
                return False
            self.update_history(i)
        elif len(possible) != 0:
            next_pos = list(possible)[0]
            pos = possible[next_pos]
            del possible[next_pos]
            if len(possible) != 0 :
                self.tosearch.append((len(self.history), possible))
            self.rotate(next_pos)
            score = self.solution_scores(self.history)
            self.score = score
            if self.best_scores[(self.position, self.orient)] == 0:
                self.best_scores[(self.position, self.orient)] = score
            elif score < self.best_scores[(self.position, self.orient)]:
                self.best_scores[(self.position, self.orient)] = score
            self.position = pos
            self.update_history(i)
    
    def check_end(self):
        if self.position == self.exit:
            return True
        return False
    
    def complete(self):
        if len(self.tosearch) > 0:
            self.solutions.append(self.history.copy())
            self.best_score = self.solution_scores(self.history)
            self.next_path()
            self.update_history()
        else: 
            return True

    def next_path(self, i: int = 0):
        if len(self.tosearch) == 0:
            return False
        next = self.tosearch[-1]
        del self.tosearch[-1]
        self.history = self.history[0: next[0]]
        self.orient_history = self.orient_history[0:next[0]]
        self.position = self.history[next[0] - 1]
        self.orient = self.orient_history[next[0] - 1]
        next_pos = list(next[1])[0]
        self.rotate(next_pos)
        score = self.solution_scores(self.history)
        self.score = score
        if self.best_scores[(self.position, self.orient)] == 0:
            self.best_scores[(self.position, self.orient)] = score
        elif score < self.best_scores[(self.position, self.orient)]:
            self.best_scores[(self.position, self.orient)] = score
        self.position = next[1][next_pos]

    def rotate(self, new_orient: tuple):
        index = self.orientations.index(self.orient)
        if new_orient == self.orientations[(index + 1) % 4]:
            self.history.append('A')
        elif new_orient == self.orientations[(index + 2) % 4]:
            self.history + ['A', 'A']
            self.orient_history.append('A')
        elif new_orient == self.orientations[(index + 3) % 4]:
            self.history.append('C')
        self.orient = new_orient
        self.orient_history.append(self.orient)
    
    def update_history(self, i: int = 0):
        self.history.append(self.position)
        self.orient_history.append(self.orient)
        score = self.solution_scores(self.history)
        self.score = score
        if score > self.best_score:
            next= self.next_path(i)
            if next == False:
                return False
            self.update_history(i)
        elif self.best_scores[(self.position, self.orient)] == 0:
            self.best_scores[(self.position, self.orient)] = score
        elif score < self.best_scores[(self.position, self.orient)]:
            self.best_scores[(self.position, self.orient)] = score
        elif score >= self.best_scores[(self.position, self.orient)]: ##here 
            next= self.next_path(i)
            if next == False:
                return False
            self.update_history(i)

    def show_map(self, visited: list = []):
        for i in range(self.height):
            for j in range(self.width):
                if (i,j) in self.walls:
                    print('#',end='')
                elif (i,j) == self.position:
                    print(self.orient_pic[self.orient],end='')
                elif (i,j) == self.exit:
                    print('E',end='')
                elif (i,j) in visited:
                    print('v',end='')
                else:
                    print('.',end='')
            print()
    
    def solution_scores(self, solution: list):
        score = 0
        for step in solution:
            if step in ['A', 'C']:
                score += 1000
            else:
                score += 1
        return score -1
    
    def all_scores(self):
        scores = []
        for solution in self.solutions:
            scores.append(self.solution_scores(solution))
        return sorted(scores)
    
    def in_best(self):
        result = set()
        to_check = []
        pos = (self.exit, (0,1))
        result.add(pos[0])
        score = self.best_score
        to_check += self.adjacent(pos[0],pos[1], score)
        for i in range(1000000):
            if len(to_check) == 0:
                break
            check = to_check[-1]
            #print(i,check, self.best_scores[(check[0],check[1])])
            del to_check[-1]
            if self.best_scores[(check[0],check[1])] == check[2]:
                pos = (check[0],check[1])
                result.add(pos[0])
                score = check[2]
                to_check += self.adjacent(pos[0],pos[1], score)
        print(len(result))
        return list(result)


    def adjacent(self, pos: tuple, orientation: tuple, score: int):
        result = []
        for i in self.orientations:
            coord = add(pos, i)
            if coord not in self.walls:
                if orientation == (-i[0],-i[1]):
                    result.append((coord, (-i[0],-i[1]), score - 1))
                else:
                    result.append((coord, (-i[0],-i[1]), score - 1001))
        return result


        

if __name__ == "__main__":
    maze = convert(test)
    solver = MazeSolver(maze[0],maze[1],maze[2],maze[3],maze[4])
    #solver.show_map()
    for i in range(300000000000):
        if i % 1000 == 0:
            print(i)
        if solver.check_end() == True:
            complete = solver.complete()
            if complete == True:
                print(i, f'{len(solver.solutions)}')
                print(solver.all_scores())
                print('Complete!')
                break
            #print(i, len(solver.tosearch), solver.position)
            #solver.show_map()
            continue
        move = solver.move_step()
        if move == False:
            print(i, f'{len(solver.solutions)}')
            print(solver.all_scores())
            print('complete!')
            break
        #print(i, len(solver.tosearch), solver.position, len(solver.solutions), solver.best_score, solver.score, solver.orient)
        #solver.show_map()
        sleep(0)
    #print(solver.history, solver.score)


        
    
    result = solver.in_best()
    solver.show_map(list(result))
    print(len(result))
    #for k,v in sorted(dict(solver.best_scores).items()):
    #    if k[0][1] > 0 and k[0][0] == 2:
    #        print(k,v)
    #print(solver.best_scores[(3,22),(1,0)])
    