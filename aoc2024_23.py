from itertools import chain, combinations
from collections import defaultdict

test1a = ['kh-tc',
'qp-kh',
'de-cg',
'ka-co',
'yn-aq',
'qp-ub',
'cg-tb',
'vc-aq',
'tb-ka',
'wh-tc',
'yn-cg',
'kh-ub',
'ta-co',
'de-co',
'tc-td',
'tb-wq',
'wh-td',
'ta-ka',
'td-qp',
'aq-cg',
'wq-ub',
'ub-vc',
'de-ta',
'wq-aq',
'wq-vc',
'wh-yn',
'ka-de',
'kh-ta',
'co-tc',
'wh-qp',
'tb-vc',
'td-yn']

test1 = [set(x.split('-')) for x in test1a]
test1_set = set([frozenset(x) for x in test1])
test1_comp = list(set().union(*test1))
test1_comp_t = [x for x in test1_comp if x[0] == 't']

test = []
lengths = set()
with open('input23.txt') as input:
    for line in input:
        line = line.replace('\n','')
        lengths.add(len(line))
        test.append(set(line.split('-')))
test_set = set([frozenset(x) for x in test])
test_comp = list(set().union(*test))
test_comp_t = [x for x in test_comp if x[0] == 't']

def test_1():
    cycles = set()
    for m, comp in enumerate(test1_comp_t):
        if m > 20:
            break
        connections = set().union(*[x for x in test1 if comp in x])
        connections.remove(comp)
        possible = list(map(set,combinations(list(connections), 2)))
        for x in possible:
            if x in test1_set:
                y = x.copy()
                y.add(comp)
                cycles.add(frozenset(y))
    print(cycles)
    print(len(cycles))

def part_1():
    cycles = set()
    for m, comp in enumerate(test_comp_t):
        if m > 600:
            break
        connections = set().union(*[x for x in test if comp in x])
        connections.remove(comp)
        possible = list(map(set,combinations(list(connections), 2)))
        for x in possible:
            if x in test_set:
                y = x.copy()
                y.add(comp)
                cycles.add(frozenset(y))
    print(cycles)
    print(len(cycles))

def all_3_cycles(t: list, tc: list, ts: set):
    cycles = set()
    for m, comp in enumerate(tc):
        if m > 1000:
            break
        connections = set().union(*[x for x in t if comp in x])
        connections.remove(comp)
        possible = list(map(set,combinations(list(connections), 2)))
        for x in possible:
            if x in ts:
                y = x.copy()
                y.add(comp)
                cycles.add(frozenset(y))
    #print(len(cycles))
    #print(len(set().union(*cycles)))
    return cycles

def all_4_cycles(t: list, tc: list, ts: set): #just returns collections of sets with no order
    cycles = set()
    all_connections = dict()
    for m, comp in enumerate(tc):
        if m > 1000:
            break
        connections = set().union(*[x for x in t if comp in x])
        connections.remove(comp)
        all_connections[comp] = connections
    for m, comp in enumerate(tc):
        connections = all_connections[comp]
        possible = list(map(set,combinations(list(connections), 2)))
        for x in possible:
            for y in tc:
                if y == comp:
                    continue
                if x.issubset(all_connections[y]) == True:
                    z = x.copy()
                    z.add(comp)
                    z.add(y)
                    cycles.add(frozenset(z))
    #print(len(cycles))
    #print(len(set().union(*cycles)))
    #print(cycles)
    #print(len(cycles))
    return cycles


def all_4_full(cycles4: set, cycles3: set):
    full_4_cycles = []
    for cycle in cycles4:
        possible = list(map(set,combinations(list(cycle), 3)))
        possible = set([frozenset(x) for x in possible])
        if possible.issubset(cycles3):
            full_4_cycles.append(cycle.copy())
    return full_4_cycles

def all_full_vs(cycles3: set, tc: list, ts: set, m: int):
    p = m - 1
    cycles4full = set()
    cycles = list(cycles3)
    for n, cycle in enumerate(cycles):
        if n % 1000 == 0:
            print(m,n)
        for comp in tc:
            i =0
            for x in cycle:
                if {comp, x} in ts:
                    i += 1
            if i == p:
                x = set(cycle)
                x.add(comp)
                cycles4full.add(frozenset(x))
    return cycles4full

def test_2():
    cycles3 = all_3_cycles(test1, test1_comp, test1_set)
    cycles4 = all_4_cycles(test1, test1_comp, test1_set)
    a = all_4_full(cycles4, cycles3)
    print(len(cycles3))
    print(len(cycles4))
    print(len(a))

def part_2():
    #use 3 cycles to find groups of 4 with all connections: 4 with any one removed will be a three cycle
    # repeat 4 to 5 and 5 to 6
    cycles3 = all_3_cycles(test, test_comp, test_set)
    cycles4 = all_4_cycles(test, test_comp, test_set)
    a = all_4_full(cycles4, cycles3)
    print(len(cycles3))
    print(len(cycles4))
    print(len(a))

if __name__ == '__main__':
    cycles3 = all_3_cycles(test, test_comp, test_set)
    a = cycles3
    i = 4
    while True:
        if len(a) == 1:
            print(a)
            break
        a = all_full_vs(a, test_comp, test_set,i)
        print('Cycle complete', i, len(a))
        i += 1


