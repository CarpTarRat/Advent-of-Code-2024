import numpy as np
import re

data = []
with open('input13.txt') as input:
    matrix = []
    for number, line in enumerate(input):
        numbers = [int(x) for x in list(re.findall('[0123456789]+', line))]
        if numbers == []:
            continue
        if number % 4 == 0 or number % 4 == 1:
            matrix.append(numbers)
        if number % 4 == 2:
            tosolve = np.array([int(number) for number in numbers]) + np.array([10000000000000,10000000000000])
            data.append((np.transpose(np.array(matrix)),tosolve))
            matrix = []

solutions = []
for d in data:
    solutions.append(np.linalg.solve(d[0],d[1]))


solutions_int = []
for number, solution in enumerate(solutions):
    int_solution = np.array([int(round(solution[0])), int(round(solution[1]))])
    print(data[number][0], int_solution, solution, data[number][1], np.matmul(data[number][0], int_solution))
    if (np.matmul(data[number][0], int_solution) == data[number][1]).all() == True:
        solutions_int.append(int_solution)
    else:
        solutions_int.append(np.zeros(2))

price = 0
for solution in solutions_int:
    price += solution[0] * 3 + solution[1]
print(price)