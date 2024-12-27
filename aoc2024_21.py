from functools import cache

test = ['279A',
'341A',
'459A',
'540A',
'085A']

test1 = ['029A',
'980A',
'179A',
'456A',
'379A']

dpad = {'A': (0,0), '^': (1,0), '>': (0,1), 'v': (1,1), '<': (2,1)}

npad = {'A': (0,0), '0': (1,0), '3': (0,1), '2': (1,1), '1': (2,1), '6': (0,2), '5': (1,2), '4': (2,2), '9': (0,3), '8': (1,3), '7': (2,3)}

def l1_distance(a,b):
    return abs(a[0] - b[1]) + abs(a[1] - b[1])

def npad_full(s: str):
    result = npad_shortest('A', s[0])
    for i in range(len(s) - 1):
        result += npad_shortest(s[i], s[i+1])
    return result

def npad_shortest(a,b):
    if a == b:
        return 1
    else:
        x = npad[b][0] - npad[a][0]
        y = npad[b][1] - npad[a][1]
        if x == 0:
            if y == -1:
                return dpad1_string_shortest('AvA')
            elif y == -2:
                return dpad1_string_shortest('AvvA')
            elif y == -3:
                return dpad1_string_shortest('AvvvA')
            elif y == 1:
                return dpad1_string_shortest('A^A')
            elif y == 2:
                return dpad1_string_shortest('A^^A')
            elif y == 3:
                return dpad1_string_shortest('A^^^A')
        elif x == 1:
            if y == 0:
                return dpad1_string_shortest('A<A')
            elif y == 1:
                if a == '0':
                    return dpad1_string_shortest('A^<A')
                else:
                    return min(dpad1_string_shortest('A<^A'), dpad1_string_shortest('A^<A'))
            elif y == 2:
                if a == '0':
                    return min(dpad1_string_shortest('A^<^A'), dpad1_string_shortest('A^^<A'))
                else:
                    return min(dpad1_string_shortest('A<^^A'), dpad1_string_shortest('A^<^A'), dpad1_string_shortest('A^^<A'))
            elif y == 3:
                if a == '0':
                    return min(dpad1_string_shortest('A^<^^A'), dpad1_string_shortest('A^^<^A'), dpad1_string_shortest('A^^^<A'))
                else:
                    return min(dpad1_string_shortest('A<^^^A'), dpad1_string_shortest('A^<^^A'), dpad1_string_shortest('A^^<^A'), dpad1_string_shortest('A^^^<A'))
            elif y == -1:
                    return min(dpad1_string_shortest('A<vA'), dpad1_string_shortest('Av<A'))
            elif y == -2:
                return min(dpad1_string_shortest('A<vvA'), dpad1_string_shortest('Av<vA'), dpad1_string_shortest('Avv<A'))
            elif y == -3:
                return min(dpad1_string_shortest('A<vvvA'), dpad1_string_shortest('Av<vvA'), dpad1_string_shortest('Avv<vA'), dpad1_string_shortest('Avvv<A'))
        elif x == 2:
            if y == 0:
                return dpad1_string_shortest('A<<A')
            elif y == 1:
                if a == 'A':
                    return min(dpad1_string_shortest('A^<<A'), dpad1_string_shortest('A<^<A'))
                else:
                    return min(dpad1_string_shortest('A^<<A'), dpad1_string_shortest('A<^<A'), dpad1_string_shortest('A<<^A'))
            elif y == 2:
                if a == 'A':
                    return min(dpad1_string_shortest('A^^<<A'), dpad1_string_shortest('A^<^<A'), dpad1_string_shortest('A^<<^A'), dpad1_string_shortest('A<^<^A'))
                else: 
                    return min(dpad1_string_shortest('A^^<<A'), dpad1_string_shortest('A^<^<A'), dpad1_string_shortest('A^<<^A'), dpad1_string_shortest('A<^<^A'), dpad1_string_shortest('A<<^^A'))
            elif y == 3:
                return min(dpad1_string_shortest('A^^^<<A'), dpad1_string_shortest('A^^<^<A'), dpad1_string_shortest('A^<^^<A'), dpad1_string_shortest('A<^^^<A'), dpad1_string_shortest('A<^^<^A'), dpad1_string_shortest('A<^<^^A') )
            elif y == -1:
                return min(dpad1_string_shortest('Av<<A'), dpad1_string_shortest('A<v<A'), dpad1_string_shortest('A<<vA'))
            elif y == -2:
                return min(dpad1_string_shortest('Avv<<A'), dpad1_string_shortest('Av<v<A'), dpad1_string_shortest('Av<<vA'), dpad1_string_shortest('A<v<vA'), dpad1_string_shortest('A<<vvA'))
        elif x == -2:
            if y == 0:
                return dpad1_string_shortest('A>>A')
            elif y == 1:
                return min(dpad1_string_shortest('A^>>A'), dpad1_string_shortest('A>^>A'), dpad1_string_shortest('A>>^A'))
            elif y == 2:
                return min(dpad1_string_shortest('A^^>>A'), dpad1_string_shortest('A^>^>A'), dpad1_string_shortest('A^>>^A'), dpad1_string_shortest('A>^>^A'), dpad1_string_shortest('A>>^^A'))
            elif y == -1:
                if a == '1':
                    return min(dpad1_string_shortest('A>v>A'), dpad1_string_shortest('A>>vA'))
                else:
                    return min(dpad1_string_shortest('Av>>A'), dpad1_string_shortest('A>v>A'), dpad1_string_shortest('A>>vA'))
            elif y == -2:
                if a == '4':
                    return min(dpad1_string_shortest('Av>v>A'), dpad1_string_shortest('Av>>vA'), dpad1_string_shortest('A>v>vA'), dpad1_string_shortest('A>>vvA'))
                else:
                    return min(dpad1_string_shortest('Avv>>A'), dpad1_string_shortest('Av>v>A'), dpad1_string_shortest('Av>>vA'), dpad1_string_shortest('A>v>vA'), dpad1_string_shortest('A>>vvA'))
            elif y == -3:
                return min(dpad1_string_shortest('A>>vvvA'), dpad1_string_shortest('A>v>vvA'), dpad1_string_shortest('A>vv>vA'), dpad1_string_shortest('A>vvv>A'), dpad1_string_shortest('Av>vv>A'), dpad1_string_shortest('Avv>v>A'))
        elif x == -1:
            if y == 0:
                return dpad1_string_shortest('A>A')
            elif y == 1:
                return min(dpad1_string_shortest('A>^A'), dpad1_string_shortest('A^>A'))
            elif y == 2:
                return min(dpad1_string_shortest('A>^^A'), dpad1_string_shortest('A^>^A'), dpad1_string_shortest('A^^>A'))
            elif y == 3:
                return min(dpad1_string_shortest('A>^^^A'), dpad1_string_shortest('A^>^^A'), dpad1_string_shortest('A^^>^A'), dpad1_string_shortest('A^^^>A'))
            elif y == -1:
                if a == '1':
                    return dpad1_string_shortest('A>vA')
                else:
                    return min(dpad1_string_shortest('A>vA'), dpad1_string_shortest('Av>A'))
            elif y == -2:
                if a == '4':
                    return min(dpad1_string_shortest('A>vvA'), dpad1_string_shortest('Av>vA'))
                else:
                    return min(dpad1_string_shortest('A>vvA'), dpad1_string_shortest('Av>vA'), dpad1_string_shortest('Avv>A'))
            elif y == -3:
                if a == '7':
                    return min(dpad1_string_shortest('A>vvvA'), dpad1_string_shortest('Av>vvA'), dpad1_string_shortest('Avv>vA'))
                else:
                    return min(dpad1_string_shortest('A>vvvA'), dpad1_string_shortest('Av>vvA'), dpad1_string_shortest('Avv>vA'), dpad1_string_shortest('Avvv>A'))

def dpad1_string_shortest(s: str):
    result = 0
    for i in range(len(s) - 1):
        result += dpad1_shortest(s[i], s[i+1])
    return result

def dpad1_shortest(a,b):
    if a == b:
        return 1
    else:
        x = dpad[b][0] - dpad[a][0]
        y = dpad[b][1] - dpad[a][1]
        if x == 0:
            if y == 1:
                return dpad2_string_shortest('AvA')
            elif y == -1:
                return dpad2_string_shortest('A^A')
        elif x == 1:
            if y == 0:
                return dpad2_string_shortest('A<A')
            elif y == 1:
                if a == '^':
                    return dpad2_string_shortest('Av<A')
                else:
                    return min(dpad2_string_shortest('A<vA'), dpad2_string_shortest('Av<A'))
            elif y == -1:
                return min(dpad2_string_shortest('A<^A'), dpad2_string_shortest('A^<A'))
        elif x == 2:
            if y == 0:
                return dpad2_string_shortest('A<<A')
            elif y == 1:
                return min(dpad2_string_shortest('Av<<A'), dpad2_string_shortest('A<v<A'))
        elif x == -2:
            if y == 0:
                return dpad2_string_shortest('A>>A')
            elif y == -1:
                return min(dpad2_string_shortest('A>>^A'), dpad2_string_shortest('A>^>A'))
        elif x == -1:
            if y == 0:
                return dpad2_string_shortest('A>A')
            elif y == 1:
                return min(dpad2_string_shortest('A>vA'), dpad2_string_shortest('Av>A'))
            elif y == -1:
                if a == '<':
                    return dpad2_string_shortest('A>^A')
                else:
                    return min(dpad2_string_shortest('A>^A'), dpad2_string_shortest('A^>A'))

def dpad2_string_shortest(s: str):
    result = 0
    for i in range(len(s) - 1):
        result += dpad2_shortest(s[i], s[i+1])
    return result

def dpad2_shortest(a,b): # including final press no initial press, from a to b
    if a == b:
        return 1
    else:
        x = dpad[b][0] - dpad[a][0]
        y = dpad[b][1] - dpad[a][1]
        if x == 0:
            return dpad3_string_shortest('vA')
        elif x == 1:
            if y == 0:
                return dpad3_string_shortest('<A')
            elif y == 1:
                return min(dpad3_string_shortest('<vA'), dpad3_string_shortest('v<A'))
            elif y == -1:
                return min(dpad3_string_shortest('<^A'), dpad3_string_shortest('^<A'))
        elif x == 2:
            if y == 0:
                return dpad3_string_shortest('<<A')
            elif y == 1:
                return min(dpad3_string_shortest('v<<A'), dpad3_string_shortest('<v<A'))
        elif x == -2:
            if y == 0:
                return dpad3_string_shortest('>>A')
            elif y == -1:
                return min(dpad3_string_shortest('>>^A'), dpad3_string_shortest('>^>A'))
        elif x == -1:
            if y == 0:
                return dpad3_string_shortest('>A')
            elif y == 1:
                return min(dpad3_string_shortest('>vA'), dpad3_string_shortest('v>A'))
            elif y == -1:
                if a == '<':
                    return dpad3_string_shortest('>^A')
                else:
                    return min(dpad3_string_shortest('>^A'), dpad3_string_shortest('^>A'))

def dpad3_string_shortest(s: str): #fix
    return len(s)

def part_1():
    result = 0
    for x in test:
        result += int(x[0:3]) * npad_full(x)
        print(x, int(x[0:3]), npad_full(x))
    print(result)

def test_1():
    result = 0
    for x in test1:
        result += int(x[0:3]) * npad_full(x)
        print(x, npad_full(x))
    print(result)








def npad_full2(s: str):
    result = npad_shortest2('A', s[0])
    for i in range(len(s) - 1):
        result += npad_shortest2(s[i], s[i+1])
    return result

def npad_shortest2(a,b):
    if a == b:
        return 1
    else:
        x = npad[b][0] - npad[a][0]
        y = npad[b][1] - npad[a][1]
        if x == 0:
            if y == -1:
                return dpad_string_shortest('AvA', 1)
            elif y == -2:
                return dpad_string_shortest('AvvA', 1)
            elif y == -3:
                return dpad_string_shortest('AvvvA', 1)
            elif y == 1:
                return dpad_string_shortest('A^A', 1)
            elif y == 2:
                return dpad_string_shortest('A^^A', 1)
            elif y == 3:
                return dpad_string_shortest('A^^^A', 1)
        elif x == 1:
            if y == 0:
                return dpad_string_shortest('A<A', 1)
            elif y == 1:
                if a == '0':
                    return dpad_string_shortest('A^<A', 1)
                else:
                    return min(dpad_string_shortest('A<^A', 1), dpad_string_shortest('A^<A', 1))
            elif y == 2:
                if a == '0':
                    return min(dpad_string_shortest('A^<^A', 1), dpad_string_shortest('A^^<A', 1))
                else:
                    return min(dpad_string_shortest('A<^^A', 1), dpad_string_shortest('A^<^A', 1), dpad_string_shortest('A^^<A', 1))
            elif y == 3:
                if a == '0':
                    return min(dpad_string_shortest('A^<^^A', 1), dpad_string_shortest('A^^<^A', 1), dpad_string_shortest('A^^^<A', 1))
                else:
                    return min(dpad_string_shortest('A<^^^A', 1), dpad_string_shortest('A^<^^A', 1), dpad_string_shortest('A^^<^A', 1), dpad_string_shortest('A^^^<A', 1))
            elif y == -1:
                    return min(dpad_string_shortest('A<vA', 1), dpad_string_shortest('Av<A', 1))
            elif y == -2:
                return min(dpad_string_shortest('A<vvA', 1), dpad_string_shortest('Av<vA', 1), dpad_string_shortest('Avv<A', 1))
            elif y == -3:
                return min(dpad_string_shortest('A<vvvA', 1), dpad_string_shortest('Av<vvA', 1), dpad_string_shortest('Avv<vA', 1), dpad_string_shortest('Avvv<A', 1))
        elif x == 2:
            if y == 0:
                return dpad_string_shortest('A<<A', 1)
            elif y == 1:
                if a == 'A':
                    return min(dpad_string_shortest('A^<<A', 1), dpad_string_shortest('A<^<A', 1))
                else:
                    return min(dpad_string_shortest('A^<<A', 1), dpad_string_shortest('A<^<A', 1), dpad_string_shortest('A<<^A', 1))
            elif y == 2:
                if a == 'A':
                    return min(dpad_string_shortest('A^^<<A', 1), dpad_string_shortest('A^<^<A', 1), dpad_string_shortest('A^<<^A', 1), dpad_string_shortest('A<^<^A', 1))
                else: 
                    return min(dpad_string_shortest('A^^<<A', 1), dpad_string_shortest('A^<^<A', 1), dpad_string_shortest('A^<<^A', 1), dpad_string_shortest('A<^<^A', 1), dpad_string_shortest('A<<^^A', 1))
            elif y == 3:
                return min(dpad_string_shortest('A^^^<<A', 1), dpad_string_shortest('A^^<^<A', 1), dpad_string_shortest('A^<^^<A', 1), dpad_string_shortest('A<^^^<A', 1), dpad_string_shortest('A<^^<^A', 1), dpad_string_shortest('A<^<^^A', 1) )
            elif y == -1:
                return min(dpad_string_shortest('Av<<A', 1), dpad_string_shortest('A<v<A', 1), dpad_string_shortest('A<<vA', 1))
            elif y == -2:
                return min(dpad_string_shortest('Avv<<A', 1), dpad_string_shortest('Av<v<A', 1), dpad_string_shortest('Av<<vA', 1), dpad_string_shortest('A<v<vA', 1), dpad_string_shortest('A<<vvA', 1))
        elif x == -2:
            if y == 0:
                return dpad_string_shortest('A>>A', 1)
            elif y == 1:
                return min(dpad_string_shortest('A^>>A', 1), dpad_string_shortest('A>^>A', 1), dpad_string_shortest('A>>^A', 1))
            elif y == 2:
                return min(dpad_string_shortest('A^^>>A', 1), dpad_string_shortest('A^>^>A', 1), dpad_string_shortest('A^>>^A', 1), dpad_string_shortest('A>^>^A', 1), dpad_string_shortest('A>>^^A', 1))
            elif y == -1:
                if a == '1':
                    return min(dpad_string_shortest('A>v>A', 1), dpad_string_shortest('A>>vA', 1))
                else:
                    return min(dpad_string_shortest('Av>>A', 1), dpad_string_shortest('A>v>A', 1), dpad_string_shortest('A>>vA', 1))
            elif y == -2:
                if a == '4':
                    return min(dpad_string_shortest('Av>v>A', 1), dpad_string_shortest('Av>>vA', 1), dpad_string_shortest('A>v>vA', 1), dpad_string_shortest('A>>vvA', 1))
                else:
                    return min(dpad_string_shortest('Avv>>A', 1), dpad_string_shortest('Av>v>A', 1), dpad_string_shortest('Av>>vA', 1), dpad_string_shortest('A>v>vA', 1), dpad_string_shortest('A>>vvA', 1))
            elif y == -3:
                return min(dpad_string_shortest('A>>vvvA', 1), dpad_string_shortest('A>v>vvA', 1), dpad_string_shortest('A>vv>vA', 1), dpad_string_shortest('A>vvv>A', 1), dpad_string_shortest('Av>vv>A', 1), dpad_string_shortest('Avv>v>A', 1))
        elif x == -1:
            if y == 0:
                return dpad_string_shortest('A>A', 1)
            elif y == 1:
                return min(dpad_string_shortest('A>^A', 1), dpad_string_shortest('A^>A', 1))
            elif y == 2:
                return min(dpad_string_shortest('A>^^A', 1), dpad_string_shortest('A^>^A', 1), dpad_string_shortest('A^^>A', 1))
            elif y == 3:
                return min(dpad_string_shortest('A>^^^A',1), dpad_string_shortest('A^>^^A', 1), dpad_string_shortest('A^^>^A', 1), dpad_string_shortest('A^^^>A', 1))
            elif y == -1:
                if a == '1':
                    return dpad_string_shortest('A>vA', 1)
                else:
                    return min(dpad_string_shortest('A>vA', 1), dpad_string_shortest('Av>A', 1))
            elif y == -2:
                if a == '4':
                    return min(dpad_string_shortest('A>vvA', 1), dpad_string_shortest('Av>vA', 1))
                else:
                    return min(dpad_string_shortest('A>vvA', 1), dpad_string_shortest('Av>vA', 1), dpad_string_shortest('Avv>A', 1))
            elif y == -3:
                if a == '7':
                    return min(dpad_string_shortest('A>vvvA', 1), dpad_string_shortest('Av>vvA', 1), dpad_string_shortest('Avv>vA', 1))
                else:
                    return min(dpad_string_shortest('A>vvvA', 1), dpad_string_shortest('Av>vvA', 1), dpad_string_shortest('Avv>vA', 1), dpad_string_shortest('Avvv>A', 1))

@cache
def dpad_string_shortest(s: str, n :int):
    if n == 26:
        return len(s)
    result = 0
    for i in range(len(s) - 1):
        result += dpad_shortest(s[i], s[i+1], n)
    return result

@cache
def dpad_shortest(a, b, n: int):
    if n == 26 - 1:
        if a == b:
            return 1
        else:
            x = dpad[b][0] - dpad[a][0]
            y = dpad[b][1] - dpad[a][1]
            if x == 0:
                if y == 1:
                    return dpad_string_shortest('vA', n+1)
                elif y == -1:
                    return dpad_string_shortest('^A', n+1)
            elif x == 1:
                if y == 0:
                    return dpad_string_shortest('<A', n+1)
                elif y == 1:
                    if a == '^':
                        return dpad_string_shortest('v<A', n+1)
                    else:
                        return min(dpad_string_shortest('<vA', n+1), dpad_string_shortest('v<A', n+1))
                elif y == -1:
                    return min(dpad_string_shortest('<^A', n+1), dpad_string_shortest('^<A', n+1))
            elif x == 2:
                if y == 0:
                    return dpad_string_shortest('<<A', n+1)
                elif y == 1:
                    return min(dpad_string_shortest('v<<A', n+1), dpad_string_shortest('<v<A', n+1))
            elif x == -2:
                if y == 0:
                    return dpad_string_shortest('>>A', n+1)
                elif y == -1:
                    return min(dpad_string_shortest('>>^A', n+1), dpad_string_shortest('>^>A', n+1))
            elif x == -1:
                if y == 0:
                    return dpad_string_shortest('>A', n+1)
                elif y == 1:
                    return min(dpad_string_shortest('AvA', n+1), dpad_string_shortest('v>A', n+1))
                elif y == -1:
                    if a == '<':
                        return dpad_string_shortest('>^A', n+1)
                    else:
                        return min(dpad_string_shortest('>^A', n+1), dpad_string_shortest('^>A', n+1))
    else:
        if a == b:
            return 1
        else:
            x = dpad[b][0] - dpad[a][0]
            y = dpad[b][1] - dpad[a][1]
            if x == 0:
                if y == 1:
                    return dpad_string_shortest('AvA', n+1)
                elif y == -1:
                    return dpad_string_shortest('A^A', n+1)
            elif x == 1:
                if y == 0:
                    return dpad_string_shortest('A<A', n+1)
                elif y == 1:
                    if a == '^':
                        return dpad_string_shortest('Av<A', n+1)
                    else:
                        return min(dpad_string_shortest('A<vA', n+1), dpad_string_shortest('Av<A', n+1))
                elif y == -1:
                    return min(dpad_string_shortest('A<^A', n+1), dpad_string_shortest('A^<A', n+1))
            elif x == 2:
                if y == 0:
                    return dpad_string_shortest('A<<A', n+1)
                elif y == 1:
                    return min(dpad_string_shortest('Av<<A', n+1), dpad_string_shortest('A<v<A', n+1))
            elif x == -2:
                if y == 0:
                    return dpad_string_shortest('A>>A', n+1)
                elif y == -1:
                    return min(dpad_string_shortest('A>>^A', n+1), dpad_string_shortest('A>^>A', n+1))
            elif x == -1:
                if y == 0:
                    return dpad_string_shortest('A>A', n+1)
                elif y == 1:
                    return min(dpad_string_shortest('A>vA', n+1), dpad_string_shortest('Av>A', n+1))
                elif y == -1:
                    if a == '<':
                        return dpad_string_shortest('A>^A', n+1)
                    else:
                        return min(dpad_string_shortest('A>^A', n+1), dpad_string_shortest('A^>A', n+1))

def part_2():
    result = 0
    for x in test:
        a = npad_full2(x)
        result += int(x[0:3]) * npad_full2(x)
        print(x, int(x[0:3]), a)
    print(result)

if __name__ == "__main__":
    part_2()
    