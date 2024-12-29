from functools import cache

def gate_output(a: int, b: int, gate: str):
        if gate == 'AND':
            return a & b
        elif gate == 'OR':
            return a | b
        elif gate == 'XOR':
            return a ^ b
        
def binary_add(a: str, b: str):
    return f'{int(a, 2) + int(b, 2):46b}'

class Solution():
    def __init__(self, file: str):
        self.open_file(file)
        self.gates = list(self.wires.keys())

    def open_file(self, file: str):
        with open(file) as input:
            i = 0
            initials = dict()        
            others = dict()
            for line in input:
                line = line.replace('\n','')
                if line == '':
                    i = 1
                    continue
                if i == 0:
                    x = line.split(': ')
                    initials[x[0]] = int(x[1])
                elif i == 1:
                    x = line.split(' ')
                    others[x[4]] = (x[0], x[2], x[1])
        self.initial = initials
        self.wires = others

    def initial_input(self):
        result1 = ''
        result2 = ''
        for i in range(1000):
            gate1 = 'x' + f'{i:02d}'
            gate2 = 'y' + f'{i:02d}'
            if gate1 not in self.initial:
                break
            result1 += str(self.initial[gate1])
            result2 += str(self.initial[gate2])
        return result1, result2
    
    def swap_wires(self, gate1: str, gate2: str):
        self.wires[gate1], self.wires[gate2] = self.wires[gate2], self.wires[gate1]

    #@cache
    def output(self, gate: str):
        if gate in self.initial:
            return self.initial[gate]
        inputs = self.wires[gate]
        return gate_output(self.output(inputs[0]), self.output(inputs[1]), inputs[2])
    
    def output2(self, gate: str, v: int):
        if gate[0] == 'x' or gate[0] == 'y':
            return f'{gate}'
        inputs = self.wires[gate]
        if v == 0:
            return f'({self.output2(inputs[0], v)}) {inputs[2]} ({self.output2(inputs[1], v)})'
        else:
            return f'{inputs[0]}: ({self.output2(inputs[0], v)}) {inputs[2]} {inputs[1]}: ({self.output2(inputs[1], v)})'
    
    def output3(self, gate: str, v: int, seen: list = []):
        if gate[0] == 'x' or gate[0] == 'y':
            return f'{gate}', []
        if gate in seen:
            return f'{gate}', []
        inputs = self.wires[gate]
        seen_update = seen.copy()
        seen_update.append(inputs[0])
        seen_update.append(inputs[1])
        if v == 0:
            return f'({self.output3(inputs[0], v, seen)[0]}) {inputs[2]} ({self.output3(inputs[1], v, seen)[0]})', seen_update
        else:
            return f'{inputs[0]}: ({self.output3(inputs[0], v, seen)[0]}) {inputs[2]} {inputs[1]}: ({self.output3(inputs[1], v, seen)[0]})', seen_update
        

def test_1():
    test1 = Solution('input_test24.txt')
    result = ''
    for i in range(13):
        gate = 'z' + f'{i:02d}'
        output = test1.output(gate)
        result = str(output) + result
        print(f'{gate}: {output}')
    print(result)
    print(int(result, 2))

def part_1():
    test = Solution('input24.txt')
    test.swap_wires('hwk', 'z06')
    test.swap_wires('tnt', 'qmd')
    test.swap_wires('hpc','mjr')
    test.swap_wires('z37', 'cgr')
    j = 10
    result = ''
    for i in range(1000):
        gate = 'z' + f'{i:02d}'
        if gate not in test.wires:
            break
        output = test.output(gate)
        result = str(output) + result
        #print(f'{gate}: {output}, {test.wires[gate]}')
    print(result)
    return result
    #print(int(result, 2))

def test_2():
    test1 = Solution('input_test24.txt')
    print(test1.initial_input())

def part_2(): 
    test = Solution('input24.txt')
    a = test.initial_input()
    result = binary_add(a[0][::-1], a[1][::-1])
    print(result)
    print(a[0][::-1])
    print(a[1][::-1])

def part_2_test():
    test = Solution('input24.txt')
    test.swap_wires('hwk', 'z06')
    test.swap_wires('tnt', 'qmd')
    test.swap_wires('hpc','z31')
    test.swap_wires('z37', 'cgr')
    seen = []
    for i in range(100):
        print(i)
        gate = 'z' + f'{i:02d}'
        if gate not in test.wires:
            break
        x = test.output3(gate, 1, seen)
        seen = x[1]
        print(x[0])
        print('')

if __name__ == "__main__":
    #part_2_test()
    part_1()
    part_2()
    part_2_test()
    print(','.join(sorted(['hwk', 'z06', 'tnt', 'qmd', 'hpc','z31', 'z37', 'cgr'])))
