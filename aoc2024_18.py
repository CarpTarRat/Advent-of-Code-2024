from collections import defaultdict
import numpy as np
from time import sleep

test1 = [(5,4), (4,2), (4,5), (3,0), (2,1), (6,3), (2,4), (1,5), (0,6), (3,3), (2,6), (5,1), (1,2), (5,5), (2,5), (6,5), (1,4,),
(0,4), (6,4), (1,1), (6,1), (1,0), (0,5), (1,6), (2,0)]

test = []
with open('input18.txt') as input:
    for line in input:
        line = line.replace('\n','').split(',')
        test.append((int(line[0]),int(line[1])))

directions = [(1,0), (0,1), (-1,0), (0,-1)]

def add(a: tuple, b: tuple):
    return tuple(np.add(a,b))

class MazeSolver:
    def __init__(self, walls: list, initial: tuple, exit: tuple, height: int, width: int):
        self.position = initial
        self.all_walls = walls
        self.exit = exit
        self.width = width
        self.height = height
        self.history = [initial]
        self.tosearch = []
        self.solutions = []
        self.best_scores = defaultdict(int)
        self.best_score = 10000000000000000
        self.score = 1

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
        self.check_score()

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
            self.update_history()
    
    def check_end(self):
        if self.position == self.exit:
            return True
        return False
    
    def complete(self):
        if len(self.tosearch) > 0:
            self.solutions.append(self.history.copy())
            self.best_score = self.score
            self.next_path()
            self.update_history()
        else: 
            return True
        
    def run(self):
        for i in range(300000000000):
            if i % 20000 == 0:
                print(i, self.best_score - 1, len(self.tosearch))
            if self.check_end() == True:
                complete = self.complete()
                if complete == True:
                    print(self.best_score - 1)
                    print('Complete!')
                    break
                continue
            move = self.move_step()
            if move == False:
                print(self.best_score - 1)
                print('complete!')
                break  
    
def part_1():
    example = MazeSolver(test, (0,0), (70,70), 71, 71)
    example.set_walls(1024)
    example.show_map()
    example.run()
    example.show_map(example.solutions[-1])

def part_1_test():
    example = MazeSolver(test1, (0,0), (6,6), 7, 7)
    example.set_walls(12)
    example.show_map()
    example.run()

def part_1_test2():
    example = MazeSolver([((0,1))], (0,0), (4,4), 5, 5)
    example.set_walls(1)
    example.show_map()
    example.run()
    example.show_map(example.solutions[-1])

def part_2():
    for i in range(3000):
        example = MazeSolver(test, (0,0), (70,70), 71, 71)
        example.set_walls(3450-i) #total 3450 possible walls, test until find a solutions
        example.run()
        if len(example.solutions) > 0:
            print(3450 - i)
            example.show_map(example.solutions[-1])
            print(example.all_walls[-i])
            break
        else:
            print(3450 - i, 'No solutions')

if __name__ == "__main__":
    part_2()
