from collections import defaultdict
from copy import copy

stones = []
with open('input11.txt') as input:
    for number,line in enumerate(input):
        line = line.replace('\n','')
        stones += [int(x) for x in line.split(' ')]

class Stones:
    def __init__(self, stones: list):
        self.stones = stones

    def pointwise_step(self, position: int):
        s = str(self.stones[position])
        length = len(s)
        if self.stones[position] == 0:
            self.stones[position] = 1
            return 0
        elif length % 2 == 0:
            self.stones[position] = int(s[0:length // 2])
            self.stones.insert(position + 1, int(s[length // 2:]))
            return 1
        else:
            self.stones[position] *= 2024
            return 0
        
    def sum(self):
        return sum((self.stones))
        
    def __str__(self):
        return f'{self.stones}'
    
    def __len__(self):
        return len(self.stones)
    
class Stones1:
    def __init__(self, stones: list):
        self.stones = {x:1 for x in stones}
        self.newstones = defaultdict(int)

    def pointwise_step(self, number: int):
        s = str(number)
        length = len(s)
        if number == 0:
            self.newstones[1] += self.stones[0]
        elif length % 2 == 0:
            self.newstones[int(s[0:length // 2])] += self.stones[number]
            self.newstones[int(s[length // 2:])] += self.stones[number]
        else:
            self.newstones[number * 2024] += self.stones[number]

    def set_stones_as_new(self):
        self.stones = copy(self.newstones)

    def reset_newstones(self):
        self.newstones = defaultdict(int)
        
    def sum(self):
        return sum([self.stones[n] for n in self.stones])
        
    def __str__(self):
        return f'{dict(self.stones)}'
    
    def __len__(self):
        return len(self.stones)

while False:
    stones_c = Stones(stones)
    for j in range(25):
        position = 0
        length = len(stones_c)
        print(j, length)
        for i in range(length):
            print(j,i, length)
            position += stones_c.pointwise_step(position) + 1
    print(len(stones_c), stones_c.sum())

stones_d = Stones1(stones)
for j in range(75):
    for i in stones_d.stones:
        stones_d.pointwise_step(i)
    stones_d.set_stones_as_new()
    stones_d.reset_newstones()
    print(j, len(stones_d))
print(stones_d.sum())