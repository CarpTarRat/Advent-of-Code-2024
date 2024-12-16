import regex

result = 0
with open('input3.txt') as input:
    for line in input:
        correct = regex.findall('mul\([0123456789]+,[0123456789]+\)',line)
        for i in correct:
            numbers = regex.findall('[01234566789]+', i)
            result += int(numbers[0]) * int(numbers[1])
print(result)

result1 = 0
do = 1
with open('input3.txt') as input:
    for line in input:
        correct = regex.findall("mul\([0123456789]+,[0123456789]+\)|do\(\)|don't\(\)",line)
        for i in correct:
            if i == "do()":
                do = 1
                continue
            elif i == "don't()":
                do = 0
                continue
            else:
                if do == 1:
                    numbers = regex.findall('[01234566789]+', i)
                    result1 += int(numbers[0]) * int(numbers[1])
print(result1)