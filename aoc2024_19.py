from functools import cache

test1_patterns = ['r', 'wr', 'b', 'g', 'bwu', 'rb', 'gb', 'br']
test1_designs = ['brwrr',
'bggr',
'gbbr',
'rrbgbr',
'ubwu',
'bwurrg',
'brgr',
'bbrgwb']

test_patterns = []
test_designs = []
with open('input19.txt') as input:
    i = 0 
    for line in input:
        line = line.replace('\n','')
        if line == '':
            i = 1
            continue
        if i == 0:
            test_patterns = line.replace(' ','').split(',')
        elif i == 1:
            test_designs.append(line)


test_patternsg = [x for x in test_patterns if 'g' in x]
test_patterns_rest = [x for x in test_patterns if x not in test_patternsg]

def filter_patterns(design: str):
    return [x for x in test_patternsg if x in design]

def is_match(design: str, pattern: str):
    d = design.index('g')
    p = pattern.index('g')
    l = len(pattern)
    try:
        d1 = design[d-p:d]
        d2 = design[d:d+l-p]
    except IndexError:
        return False
    if d1 == pattern[0:p] and d2 == pattern[p:l]:
        return design[d+l-p:]
    else: 
        return False

def check_step(relevant: list, design: str): # design contains design in position 0 and list of remainders in position 1
    to_check = []
    for pattern in relevant:
        test = is_match(design, pattern)
        if test == False:
            continue
        elif 'g' not in test:
            return True
        else:
            to_check.append(test)
    return to_check

def part_1():
    good = []
    for number, design in enumerate(test_designs):
        to_count1 = []
        if number > 100000000:
            break
        to_check = [design]
        relevant = filter_patterns(design)
        for i in range(100000000000000):
            if len(to_check) == 0:
                break
            check = to_check.pop(-1)
            next = check_step(relevant, check)
            if next == True:
                good.append(design)
                to_count1.append(check)
                break
            else:
                to_check += next
    print(len(good))
    return good

@cache #!!!!!!!!!!!!!!!
def search_design(design: str):
    count = 0
    for pattern in test_patterns:
        l = len(pattern)
        if pattern == design:
            count += 1
        elif pattern == design[0:l]:
            count += search_design(design[l:])
    return count


def part_2():
    number_of_ways = 0
    good = part_1()
    for number, design in enumerate(good):
        if number > 10000:
            break
        n = search_design(design)
        number_of_ways += n
    print(number_of_ways)

def test():
    for design in test1_designs:
        n = search_design(design)
        print(design, n)
    
if __name__ == "__main__":
    part_2()




