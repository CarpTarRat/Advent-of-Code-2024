from collections import defaultdict

grid = []
with open('input8.txt') as input:
    for line in input:
        line = line.replace('\n','')
        grid.append(list(line))
print(len(grid),len(grid[0]))

letters = defaultdict(list)
for number, row in enumerate(grid):
    for column, letter in enumerate(row):
        if letter != '.':
            letters[letter].append((number, column))

nodes = set()
for letter in letters:
    for i in range(len(letters[letter]) - 1):
        for j in range(i + 1, len(letters[letter])):
            difference_row = letters[letter][i][0] - letters[letter][j][0]
            difference_c = letters[letter][i][1] - letters[letter][j][1]
            node1 = (letters[letter][i][0] + difference_row, letters[letter][i][1] +difference_c)
            node2 = (letters[letter][j][0] - difference_row, letters[letter][j][1] -difference_c)
            #print(letters[letter][i], letters[letter][j], node1, node2)
            if node1[0] >= 0 and node1[0] < 50 and node1[1] >= 0 and node1[1] < 50:
                nodes.add(node1)
            if node2[0] >= 0 and node2[0] < 50 and node2[1] >= 0 and node2[1] < 50:
                nodes.add(node2)
print(len(nodes))

nodes2 = set()
for letter in letters:
    for i in range(len(letters[letter]) - 1):
        for j in range(i + 1, len(letters[letter])):
            nodes2.add(letters[letter][i])
            nodes2.add(letters[letter][j])
            difference_row = letters[letter][i][0] - letters[letter][j][0]
            difference_c = letters[letter][i][1] - letters[letter][j][1]
            node_row = letters[letter][i][0] + difference_row
            node_column = letters[letter][i][1] + difference_c
            while True:
                if node_row >= 0 and node_row < 50 and node_column >= 0 and node_column < 50:
                    nodes2.add((node_row, node_column))
                else:
                    break
                node_row += difference_row
                node_column += difference_c
            node_row = letters[letter][j][0] - difference_row
            node_column = letters[letter][j][1] -difference_c
            while True:
                if node_row >= 0 and node_row < 50 and node_column >= 0 and node_column < 50:
                    nodes2.add((node_row, node_column))
                else:
                    break
                node_row -= difference_row
                node_column -= difference_c
print(len(nodes2))
