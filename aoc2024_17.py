import numpy as np

A = 53437164
B = 0
C = 0

program = (2,4,1,7,7,5,4,1,1,4,5,5,0,3,3,0)

class Computer:
    def __init__(self, A: int, B: int, C: int):
        self.A = A
        self.B = B
        self.C = C
        self.pointer = 0
        self.program: tuple = None
        self.output = []

    def combo(self, n: int):
        if n in [0,1,2,3]:
            return n
        elif n == 4:
            return self.A
        elif n == 5:
            return self.B
        elif n == 6:
            return self.C
    
    def adv(self, n: int):
        self.A = self.A // (2 ** self.combo(n))

    def bxl(self, n: int):
        self.B = self.B ^ n

    def bst(self, n: int):
        self.B = self.combo(n) % 8

    def jnz(self, n: int):
        if self.A == 0:
            self.pointer = len(self.program)
        else:
            self.pointer = n

    def bxc(self, n: int):
        self.B = self.B ^ self.C

    def out(self, n: int):
        self.output.append(self.combo(n) % 8)

    def bdv(self, n: int):
        self.B = self.A // (2 ** self.combo(n))

    def cdv(self, n: int):
        self.C = self.A // (2 ** self.combo(n))

    def instruction(self, instr: int, oper: int):
        if instr == 0:
            self.adv(oper)
            self.pointer += 2
        elif instr == 1:
            self.bxl(oper)
            self.pointer += 2
        elif instr == 2:
            self.bst(oper)
            self.pointer += 2
        elif instr == 3:
            self.jnz(oper)
        elif instr == 4:
            self.bxc(oper)
            self.pointer += 2
        elif instr == 5:
            self.out(oper)
            self.pointer += 2
        elif instr == 6:
            self.bdv(oper)
            self.pointer += 2
        elif instr == 7:
            self.cdv(oper)
            self.pointer += 2

    def enter_program(self, inp: tuple):
        self.program = inp

    def run_program(self):
        while True:
            if self.pointer >= len(self.program):
                print(f'The output is {self.output}')
                break
            self.instruction(self.program[self.pointer], self.program[self.pointer + 1])

    def __str__(self):
        return f'Register A: {self.A}\nRegister B: {self.B}\nRegister C: {self.C}\n\nProgram: {self.output}'
    
def part_1():
    test = Computer(A,B,C)
    print(test)
    test.enter_program(program)
    test.run_program()
    print(test)

mod8 = ['000', '001', '010', '011', '100', '101', '110', '111']

def find_values(check: str, j: int):
    to_check = []
    test_values = [int(x,2) for x in [check + y for y in mod8]]
    for i in test_values:
        test1 = Computer(i,B,C)
        test1.enter_program(program)
        print(np.binary_repr(i,3*j), i)
        test1.run_program()
        if test1.output[-j] == program[-j]:
            to_check.append(np.binary_repr(i,3*j))
        print(test1)
    return to_check

def part_2():
    to_check = []
    check = ''
    to_check += find_values(check, 1)
    print('to check', to_check)
    for j in range(2,17):
        new = []
        while True:
            if len(to_check) == 0:
                to_check = new.copy()
                print('to check', to_check)
                break
            check = to_check[-1]
            del to_check[-1] 
            new += find_values(check,j)
    print(sorted([int(x,2) for x in to_check]))


def test_1():
    for i in range(1,2000000000):
        if i % 1000 == 0:
            print(i)
        test1 = Computer(i,0,0)
        test1.enter_program((0,3,5,4,3,0))
        test1.run_program()
        if test1.output == list((0,3,5,4,3,0)):
            print(i, test1.output)
            break

if __name__ == "__main__":
    #part_1()
    part_2()