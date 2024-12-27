from collections import defaultdict
import numpy as np

test = []
with open('input20.txt') as input:
    for line in input:
        line = line.replace('\n','')
        test.append(line)

test1 = ['###############',
'#...#...#.....#',
'#.#.#.#.#.###.#',
'#S#...#.#.#...#',
'#######.#.#.###',
'#######.#.#...#',
'#######.#.###.#',
'###..E#...#...#',
'###.#######.###',
'#...###...#...#',
'#.#####.#.###.#',
'#.#...#.#.#...#',
'#.#.#.#.#.#.###',
'#...#...#...###',
'###############',]

def convert(test: list):
    height = len(test)
    width = len(test[0])
    walls = []
    interior_walls = []
    spaces = set()
    position = (0,0)
    exit = (0,0)
    for number, row in enumerate(test):
        for column, item in enumerate(row):
            if item == "#":
                walls.append((column, number))
                if number > 0 and number < height - 1 and column > 0 and column < width - 1:
                    interior_walls.append((column, number))
            elif item == 'E':
                exit = (column, number)
                spaces.add((column, number))
            elif item == 'S':
                position = (column, number)
                spaces.add((column, number))
            else:
                spaces.add((column, number))
    return walls, position, exit, height, width, spaces, interior_walls

directions = [(1,0), (0,1), (-1,0), (0,-1)]

def add(a: tuple, b: tuple):
    return tuple(np.add(a,b))

class MazeSolver:
    def __init__(self, walls: list, initial: tuple, exit: tuple, height: int, width: int, spaces: list):
        self.position = initial
        self.all_walls = walls
        self.spaces = spaces
        self.exit = exit
        self.width = width
        self.height = height
        self.history = [initial]
        self.tosearch = []
        self.solutions = []
        self.best_scores = defaultdict(int)
        self.best_score = 103
        self.score = 1
        self.cheats = []

    def set_walls(self, time: int):
        self.walls = self.all_walls[0:time]

    def search(self):
        neighbours =  []
        for direction in directions:
            check = add(self.position, direction)
            if check in self.walls or check in self.history or check[0] < 0 or check[0] >= self.width or check[1] < 0 or check[1] >= self.height:
                continue
            else:
                neighbours.append(check)
        return neighbours
    
    def show_map(self, visited: list = []):
        for j in range(self.height):
            for i in range(self.width):
                if (i,j) in self.walls:
                    print('#',end='')
                elif (i,j) == self.position:
                    print('@',end='')
                elif (i,j) == self.exit:
                    print('E',end='')
                elif (i,j) in visited:
                    print('O',end='')
                else:
                    print('.',end='')
            print()

    def next_path(self):
        if len(self.tosearch) == 0:
            return False
        next = self.tosearch[-1]
        del self.tosearch[-1]
        self.history = self.history[0: next[1]]
        self.position = next[0]

    def update_history(self):
        self.history.append(self.position)
        self.score = len(self.history)
        check = self.check_score()
        if check == False:
            return False

    def check_score(self):
        if self.score > self.best_score:
            next = self.next_path()
            if next == False:
                return False
            self.update_history()
        elif self.best_scores[self.position] == 0 or self.best_scores[self.position] > self.score:
            self.best_scores[self.position] = self.score
        elif self.best_scores[self.position] <= self.score:
            next = self.next_path()
            if next == False:
                return False
            self.update_history()

    def move_step(self):
        possible = self.search()
        if len(possible) == 0:
            next = self.next_path()
            if next == False:
                return False
            self.update_history()
        elif len(possible) != 0:
            next_pos = possible[0]
            del possible[0]
            for position in possible:
                self.tosearch.append((position, self.score))
            self.position = next_pos
            check = self.update_history()
            if check == False:
                return False
    
    def check_end(self):
        if self.position == self.exit:
            return True
        return False
    
    def complete(self):
        if len(self.tosearch) > 0:
            self.solutions.append(self.history.copy())
            self.score = len(self.history)
            self.best_score = len(self.history)
            if self.best_score <= 102:
                return False
            self.next_path()
            self.update_history()
        else: 
            self.score = len(self.history)
            self.best_score = len(self.history)
            if self.best_score <= 102:
                return False
            return True
        
    def run(self):
        for i in range(300000000000):
            if i % 20000 == 0 and i != 0:
                print(i, self.best_score - 1, len(self.tosearch))
            if self.best_score <= 102:
                return 1
            if self.check_end() == True:
                complete = self.complete()
                if complete == True:
                    return 0
                elif complete == False:
                    return 1
                continue
            move = self.move_step()
            if move == False:
                return 0

def cheat_positions(interior_walls: list, spaces: set):
    cheats = []    
    for wall in interior_walls:
        up = add(wall, (0,-1))
        down = add(wall, (0, 1))
        right = add(wall, (1, 0))
        left = add(wall, (-1,0))
        if up in spaces and down in spaces:
            cheats.append([up,down])
        if right in spaces and left in spaces:
            cheats.append([left,right])
    return cheats

def part_1():
    data = convert(test)
    cheats = cheat_positions(data[6], data[5])
    at_least_100 = len(cheats)
    for number, cheat in enumerate(cheats):
        solver = MazeSolver(data[0], cheat[0], cheat[1], data[3], data[4], data[5])
        solver.set_walls(len(solver.all_walls))
        at_least_100 -= solver.run()
        print(number, solver.best_score, at_least_100)

directionr = list(reversed(directions))

class DistanceFinder():
    def __init__(self, walls: list, height: int, width: int, spaces: set, initial: tuple = (1,1)):
        self.walls = set(walls)
        self.spaces = spaces
        self.width = width
        self.height = height

        self.position = initial
        self.history = [initial]
        self.path_index = dict()
        self.score = 1

    def l1_distance(self, p1: tuple, p2: tuple):
        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

    def l1_neighb(self, pos: tuple, r: int):
        neigh = []
        for i in range(r+1):
            for j in range(r+1-i):
                a = (pos[0] + i, pos[1] + j)
                b = (pos[0] - i, pos[1] - j)
                c = (pos[0] + i, pos[1] - j)
                d = (pos[0] - i, pos[1] + j)
                if a in self.spaces:
                    neigh.append(a)
                if b in self.spaces:
                    neigh.append(b)
                if c in self.spaces:
                    neigh.append(c)
                if d in self.spaces:
                    neigh.append(d)
        return list(set(neigh))

    def path_distance(self, p1: tuple, p2: tuple):
        return abs(self.path_index[p1] - self.path_index[p2])

    def search(self):
        neighbours =  []
        for direction in directions:
            check = add(self.position, direction)
            if check in self.walls or check in self.history:
                continue
            else:
                neighbours.append(check)
        return neighbours
    
    def move_step(self):
        self.path_index[self.position] = len(self.history) - 1
        possible = self.search()
        if len(possible) == 0:
            self.end()
            return False
        else:
            next_pos = possible.pop(0)
            self.position = next_pos
            self.update_history()

    def update_history(self):
        self.history.append(self.position)
        self.score = len(self.history)
    
    def end(self):
        #self.show_map(self.history)
        print(f'Score: {self.score}')

    def run(self):
        while True:
            end = self.move_step()
            if end == False:
                break

    def show_map(self, visited: list = []):
        for j in range(self.height):
            for i in range(self.width):
                if (i,j) in self.walls:
                    print('#',end='')
                elif (i,j) == self.position:
                    print('@',end='')
                elif (i,j) in visited:
                    print('O',end='')
                else:
                    print('.',end='')
            print()

def part_2():
    #all points within radius <= 20 whose distance is >= 102
    #for every point, find all points which can be rreached in 102 steps, add unordered set (initial, final) for each point, also store distance
    #only need to save forward along each history
    #use dictionary to store all known exact distances and upper bounds calculated from exact distances
    #to find each point
    #after one point done, go to adjacent point, take all distance 101 from that point (previous step counts all of them) and add a pair for all
    #adjacent points which are not already added
    #repeat
    data = convert(test)
    solver = DistanceFinder(data[0], data[3], data[4], data[5], data[1])
    solver.run()
    cheats = 0
    for n,p in enumerate(solver.spaces):
        a = solver.l1_neighb(p,20)
        for y in a:
            if solver.path_distance(p,y) >= solver.l1_distance(y,p) + 100:
                cheats +=1
        print(n,p)
    print(cheats, cheats // 2)

def test_1():
    data = convert(test1)
    solver = DistanceFinder(data[0], data[3], data[4], data[5], data[1])
    solver.run()
    cheats = 0
    for n,p in enumerate(solver.spaces):
        a = solver.l1_neighb(p,20)
        for y in a:
            if solver.path_distance(p,y) >= solver.l1_distance(y,p) + 68:
                cheats +=1
        print(n,p)
    print(cheats, cheats // 2)




if __name__ == "__main__":
    part_2()