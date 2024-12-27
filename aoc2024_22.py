from collections import defaultdict

test = []
with open('input22.txt') as input:
    for line in input:
        line = line.replace('\n', '')
        test.append(int(line))

test1 = [1,
 10,
 100,
 2024]

test2 = [1, 2, 3, 2024]

def mix(a: int, b: int):
    return a ^ b 

def prune(secret: int):
    return secret % 16777216

def process(secret: int, n: int):
    if n == 1:
        return prune(mix(64 * secret, secret))
    elif n == 2:
        return prune(mix(secret // 32, secret))
    elif n == 3:
        return prune(mix(2048 * secret, secret))
    
def generate(secret: int):
    n = secret
    for i in range(1,4):
        n = process(n, i)
    return n

def generate_n(secret: int, number: int):
    test = set()
    n = secret
    test.add(n)
    for i in range(number):
        n = generate(n)
        test.add(n) 
    return n

def part_1():
    result = 0
    for n in test:
        result += generate_n(n, 2000)
    print(result)

def prices(secret: int):
    result = []
    n = secret
    result.append(n % 10)
    for i in range(2000):
        n = generate(n)
        result.append(n % 10)
    return result

def test_2():
    sequences = defaultdict(list)
    print('start')
    for m,n in enumerate(test2):
        if m > 4:
            break
        seen = set()
        x = prices(n)
        differences = [x[i] - x[i-1] for i in range(1,2001)]
        for i in range(2001-4):
            sequence = tuple(differences[i:i+4])
            if sequence not in seen:
                seen.add(sequence)
                sequences[sequence].append(x[i+4])
    sort_sequence = sorted(list(sequences), key = lambda s: sum(sequences[s]))
    print(sort_sequence[-1], sum(sequences[sort_sequence[-1]]))
    print('end')
    
    #run over each list of prices, ordered groups of 5: for each sequece of 4 prices changes add dictionary entry for price at earliest occurence
    #repeat for every list then take the maximum over sequences of the sum of prices 

def part_2():
    sequences = defaultdict(list)
    print('start')
    for m,n in enumerate(test):
        if m > 2000:
            break
        seen = set()
        x = prices(n)
        differences = [x[i] - x[i-1] for i in range(1,2001)]
        for i in range(2001-4):
            sequence = tuple(differences[i:i+4])
            if sequence not in seen:
                seen.add(sequence)
                sequences[sequence].append(x[i+4])
    sort_sequence = sorted(list(sequences), key = lambda s: sum(sequences[s]))
    print(sort_sequence[-1], sum(sequences[sort_sequence[-1]]))
    print('end')
    
if __name__ == "__main__":
    test_2()
    part_2()