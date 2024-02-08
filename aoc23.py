from load_input import load_day
import sys
import argparse
# day 1
import time
# day 2
import numpy
# day 3
import re
# day 7
from functools import cmp_to_key
# day 8
import math

def load_input(day, dummy):
    if dummy:
        with open('{}.dummy'.format(day)) as f:
            return f.read()[:-1]
    else:
        return load_day(day)[:-1]

# 1
def day1(inp):
    def first_num(x):
        for c in x:
            if c.isnumeric():
                return c

    inp = inp.split('\n')
    calib_val = 0
    for x in inp:
        num = first_num(x)
        num += first_num(x[::-1])
        calib_val += int(num)

    print('a:', calib_val)

    # second part
    calib_val = 0
    numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight',
               'nine',
               '1', '2', '3', '4', '5', '6', '7', '8', '9']
    for x in inp:
        first = len(x)
        last = 0
        num_f = 0
        num_l = 0
        for n in numbers:
            if (i := x.find(n)) != -1:
                if min(i, first) == i:
                    first = i
                    num_f = numbers.index(n) + 1
                    if num_f > 9:
                        num_f -= 9
                i = x.rfind(n)
                if max(i, last) == i:
                    last = i
                    num_l = numbers.index(n) + 1
                    if num_l > 9:
                        num_l -= 9
        calib_val += int(str(num_f)+str(num_l))

    print('b:', calib_val)

# 2
def day2(inp):
    possible = {'red':12, 'green':13, 'blue':14}
    counting = 0
    power = 0

    def is_count(dic):
        for x in possible.keys():
            if x not in dic or possible[x] < dic[x]:
                return False
        return True

    inp = [x.split(': ')[1].split('; ') for x in inp.split('\n')]
    for i, line in enumerate(inp):
        dic = {}
        for x in line:
            for val in x.split(', '):
                tmp = val.split(' ')
                if tmp[1] in dic.keys():
                    if int(tmp[0]) > dic[tmp[1]]:
                        dic[tmp[1]] = int(tmp[0])
                else:
                    dic.update({tmp[1]:int(tmp[0])})
        if is_count(dic):
            counting += i+1
        power += numpy.prod(list(dic.values()))
    print('a:', counting)
    print('b:', power)

# 3
def day3(inp):
    numbers = [list(filter(None, re.split(r'\D+', x))) for x in inp.split('\n')]
    n_indexes = [[] for _ in inp]

    for xi, x in enumerate(inp):
        for ci, c in enumerate(x):
            if c.isnumeric() and (ci == 0 or not x[ci-1].isnumeric()):
                n_indexes[xi].append(ci)

    a_sum = 0
    b_sum = 0

    for i, x in enumerate(inp):
        for ci, c in enumerate(x):
            if c != '.' and not c.isnumeric():
                gear_ratio = 1
                gear = 0
                for r in range(-1, 2):
                    try:
                        if len(numbers[i+r]) != 0:
                            for ni, n in enumerate(numbers[i+r]):
                                n_index = n_indexes[i+r][ni]
                                if n_index <= ci+1 and n_index+len(n)-1 >= ci-1:
                                    if c == '*':
                                        gear += 1
                                        gear_ratio *= int(n)
                                    a_sum += int(n)
                    #index issue
                    except:
                        pass
                if gear == 2:
                    b_sum += gear_ratio
    print('a:', a_sum)
    print('b:', b_sum)

# 4
def day4(inp):
    inp = [x.split(': ')[1].split(' | ') for x in inp.split('\n')]
    inp = [list(filter(None, x[0].split(' ') + x[1].split(' '))) for x in inp]

    a_sum = 0
    b_sum = len(inp)
    #the first has no copies
    cards = []

    for x in inp:
        s = len(x) - len(set(x))
        try:
            copies = cards.pop(0)
            b_sum += copies
        except:
            copies = 0
        if s != 0:
            a_sum += 2**(s-1)
            for i in range(s):
                try:
                    cards[i] += 1+copies
                except:
                    cards.append(1+copies)

    print('a:', a_sum)
    print('b:', b_sum)

# 5
def day5(inp):
    inp = inp.split('\n\n')
    seeds = [int(x) for x in inp.pop(0).split(': ')[1].split()]

    inp = [[[int(i) for i in y.split()] for y in x.split(':\n')[1].split('\n')] for x in inp]

    a = []
    b = 1

    def convert(num_in, map_in):
        for m in map_in:
            tmp = num_in-m[1]
            if num_in >= m[1] and tmp <= m[2]:
                return m[0]+tmp
        return num_in

    for s in seeds:
        tmp = s
        for mapping in inp:
            tmp = convert(tmp, mapping)
        a.append(tmp)

    print('a:', min(a))

    def convert_reverse(num_in, map_in):
        for m in map_in:
            tmp = num_in-m[0]
            if num_in >= m[0] and tmp <= m[2]:
                return m[1]+tmp
        return num_in

    seed_n = seeds[::2]
    seed_ranges = seeds[1::2]
    inp_rev = inp[::-1]
    while True:
        tmp = b
        for mapping in inp_rev:
            tmp = convert_reverse(tmp, mapping)
        for i, s in enumerate(seed_n):
            if tmp >= s and tmp <= s+seed_ranges[i]:
                print('b:', b)
                exit(0)
        b += 1

# 6
def day6(inp):
    inp = [[int(i) for i in x.split(': ')[1].split()] for x in inp.split('\n')]

    distance_cur = 0
    time_cur = 0

    def go_down(ms):
        if ms == 0 or ms*(time_cur-ms) <= distance_cur:
            return 0
        return 1 + go_down(ms-1)

    a_mul = 1

    def func():
        tmp = go_down(time_cur//2)*2
        if time_cur % 2 == 0:
            tmp -= 1
        return tmp

    for i, x in enumerate(inp[0]):
        distance_cur = inp[1][i]
        time_cur = x
        a_mul *= func()

    print('a:', a_mul)

    distance_cur = int(''.join([str(x) for x in inp[1]]))
    time_cur = int(''.join([str(x) for x in inp[0]]))
    b = time_cur//2

    # because of max recursion error
    while b != 0 and b*(time_cur-b) > distance_cur:
        b -= 1

    b = (time_cur//2-b)*2
    if time_cur % 2 == 0:
        b -= 1

    print('b:', b)

# 7
def day7(inp):
    inp = inp.split()
    hands = inp[::2]
    bids = inp[1::2]
    bids = {hands[i]:int(b) for i,b in enumerate(bids)}

    def hand_type(hand):
        hand_set = list(set(hand))
        set_len = len(hand_set)
        # five of a kind
        if set_len == 1:
            return 7
        elif set_len == 2:
            tmp = hand.count(hand_set[0])
            # four of a kind
            if tmp == 1 or tmp == 4:
                return 6
            # full house
            return 5
        elif set_len == 3:
            tmp1 = hand.count(hand_set[0])
            tmp2 = hand.count(hand_set[1])
            tmp3 = hand.count(hand_set[2])
            # three of a kind
            if tmp1 == 3 or tmp2 == 3 or tmp3 == 3:
                return 4
            # two pair
            return 3
        elif set_len == 5:
            # high card
            return 1
        # one pair
        return 2

    def hand_type_joker(hand):
        if hand.find('J') == -1:
            return hand_type(hand)
        hand_set = list(set(hand))
        joker_n = hand.count('J')
        del hand_set[hand_set.index('J')]
        set_len = len(hand_set)
        # five of a kind
        if set_len == 1 or set_len == 0:
            return 7
        # one pair
        elif set_len == 4:
            return 2
        max_n = 0
        max_c = -1
        for i, x in enumerate(hand_set):
            tmp = hand.count(x)
            if tmp > max_n:
                max_n = tmp
                max_c = i
        del hand_set[max_c]
        set_len -= 1
        if set_len == 1:
            # four of a kind
            if hand.count(hand_set[0]) == 1:
                return 6
            # full house
            return 5
        elif set_len == 2:
            # three of a kind
            if hand.count(hand_set[0]) == 1 and hand.count(hand_set[1]) == 1:
                return 4
            # two pair
            return 3

    cards = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']

    def hand_cmp(h1, h2):
        for i, x in enumerate(h1):
            if cards.index(x) > cards.index(h2[i]):
                return 1
            elif cards.index(x) < cards.index(h2[i]):
                return -1
        return 0

    hands.sort(key=cmp_to_key(hand_cmp))
    hands.sort(key=hand_type)
    a_sum = sum([bids[h]*(i+1) for i,h in enumerate(hands)])

    print('a:', a_sum)

    cards = ['J', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'Q', 'K', 'A']

    hands.sort(key=cmp_to_key(hand_cmp))
    hands.sort(key=hand_type_joker)
    b_sum = sum([bids[h]*(i+1) for i,h in enumerate(hands)])

    print('b:', b_sum)

# 8
def day8(inp):
    inp = inp.split('\n\n')
    instr = inp[0].replace('L', '0').replace('R', '1')
    inp = inp[1].split('\n')
    inp = {x.split(' =')[0]:x.split('(')[1].split(')')[0].split(', ') for x in inp}

    steps = 0
    current = 'AAA'
    while True:
        for i in instr:
            current = inp[current][int(i)]
            steps += 1
            if current == 'ZZZ':
                print('a:', steps)
                break
        if current == 'ZZZ':
            break

    current_b = [x for x in inp.keys() if x[2] == 'A']
    cb_len = len(current_b)
    steps_b = []
    steps = 0
    ci = 0

    while True:
        for i in instr:
            current_b[ci] = inp[current_b[ci]][int(i)]
            steps += 1
            if current_b[ci][2] == 'Z':
                ci += 1
                steps_b.append(steps)
                steps = 0
                break
        if ci == cb_len:
            break
    print('b:', math.lcm(*steps_b))

# 9
def day9(inp):
    inp = [[int(i) for i in x.split(' ')] for x in inp.split('\n')]
    a_sum = 0
    b_sum = 0

    for x in inp:
        down = []
        i = 0
        down.append(x)
        while len(set(down[i])) != 1:
            down.append([d-down[i][di] for di,d in enumerate(down[i][1:])])
            i += 1
        inc = down[-1][-1]
        first = down[-1][0]
        for d in down[::-1][1:]:
            inc += d[-1]
            first = d[0] - first
        a_sum += inc
        b_sum += first

    print('a:', a_sum)
    print('b:', b_sum)

# 10
def day10(inp):
    NORTH = 0
    SOUTH = 1
    WEST = 2
    EAST = 3

    start_compatible = {NORTH:['|', 'F', '7'],
                        SOUTH:['|', 'L', 'J'],
                        WEST:['-', 'F', 'L'],
                        EAST:['-', '7', 'J']}

    # directions:
    # 0 - north
    # 1 - south
    # 2 - west
    # 3 - east
    def is_valid(src, dst, direction):
        if dst == '.' or dst == 'S':
            return False
        if src == 'S' and dst in start_compatible[direction]:
            return True
        if src == '|':
            # north or south
            if dst == src and (direction <= SOUTH):
                return True
            elif dst == 'F' or dst == '7':
                if direction == NORTH:
                    return True
                return False
            elif dst == 'L' or dst == 'J':
                if direction == SOUTH:
                    return True
                return False
            return False
        elif src == '-':
            if dst == src and (direction >= WEST):
                return True
            elif dst == 'F' or dst == 'L':
                if direction == WEST:
                    return True
                return False
            elif dst == '7' or dst == 'J':
                if direction == EAST:
                    return True
                return False
            return False
        if dst == src:
            return False
        if src == 'F':
            if direction == SOUTH:
                if dst == 'L' or dst == 'J' or dst == '|':
                    return True
                return False
            elif direction == EAST:
                if dst == '7' or dst == 'J' or dst == '-':
                    return True
                return False
        elif src == '7':
            if direction == SOUTH:
                if dst == 'L' or dst == 'J' or dst == '|':
                    return True
                return False
            elif direction == WEST:
                if dst == 'F' or dst == 'L' or dst == '-':
                    return True
                return False
        elif src == 'L':
            if direction == NORTH:
                if dst == 'F' or dst == '7' or dst == '|':
                    return True
                return False
            elif direction == EAST:
                if dst == 'J' or dst == '7' or dst == '-':
                    return True
                return False
        # J
        else:
            if direction == NORTH:
                if dst == 'F' or dst == '7' or dst == '|':
                    return True
                return False
            elif direction == WEST:
                if dst == 'L' or dst == 'F' or dst == '-':
                    return True
                return False
        return False

    start = []
    inp = inp.split('\n')
    for ix,x in enumerate(inp):
        tmp = x.find('S')
        if tmp != -1:
            start.append(tmp)
            start.append(ix)
            break

    boundary_x = len(inp[0]) - 1
    boundary_y = len(inp) - 1

    # we don't know the direction yet
    queue = [[*start, [-1]]]
    visited = []
    visited_dir = []

    while len(queue) != 0:
        c = queue.pop(0)
        visited.append([c[0], c[1]])
        visited_dir.append(c[2])
        x = c[0]
        y = c[1]
        char = inp[y][x]
        # WEST
        if x != 0 and not [x-1, y] in visited and \
            is_valid(inp[y][x], inp[y][x-1], WEST):
                if char == 'F' or char == 'L' or char == '7' or char == 'J':
                    queue.append([x-1, y, [WEST, c[2][0]]])
                else:
                    queue.append([x-1, y, [WEST]])
        # EAST
        elif x < boundary_x and not [x+1, y] in visited and \
            is_valid(inp[y][x], inp[y][x+1], EAST):
                if char == 'F' or char == 'L' or char == '7' or char == 'J':
                    queue.append([x+1, y, [EAST, c[2][0]]])
                else:
                    queue.append([x+1, y, [EAST]])
        # NORTH
        elif y != 0 and not [x, y-1] in visited and \
            is_valid(inp[y][x], inp[y-1][x], NORTH):
                if char == 'F' or char == 'L' or char == '7' or char == 'J':
                    queue.append([x, y-1, [NORTH, c[2][0]]])
                else:
                    queue.append([x, y-1, [NORTH]])
        # SOUTH
        elif y < boundary_y and not [x, y+1] in visited and \
            is_valid(inp[y][x], inp[y+1][x], SOUTH):
                if char == 'F' or char == 'L' or char == '7' or char == 'J':
                    queue.append([x, y+1, [SOUTH, c[2][0]]])
                else:
                    queue.append([x, y+1, [SOUTH]])

    last = visited[-1]
    # WEST
    if [last[0]+1, last[1], -1] == start:
        visited_dir[0][0] = WEST
    # EAST
    elif [last[0]-1, last[1], -1] == start:
        visited_dir[0][0] = EAST
    # NORTH
    elif [last[0], last[1]-1, -1] == start:
        visited_dir[0][0] = NORTH
    # SOUTH
    elif [last[0], last[1]+1, -1] == start:
        visited_dir[0][0] = SOUTH
    # I know that my inputs S is a corner
    # detection could be made, but I won't atm
    # it is already overcomplicated
    visited_dir[0].append(visited_dir[-1][0])

    print('a:', int(len(visited)/2))

    tile_counter = 0

    visited_dir = visited_dir[1:] + visited_dir[:1]

    first_one = [min([x[0] for x in visited if x[1] == start[1]]), start[1]]
    leftmost_dir = visited_dir[visited.index(first_one)][0]
    directions = [0, 0, 0, 0]
    # what direction is the loop according to the examined pos
    if leftmost_dir == NORTH or leftmost_dir == EAST:
        directions[NORTH] = EAST
        directions[SOUTH] = WEST
        directions[WEST] = NORTH
        directions[EAST] = SOUTH
    else: # SOUTH and WEST
        directions[NORTH] = WEST
        directions[SOUTH] = EAST
        directions[WEST] = SOUTH
        directions[EAST] = NORTH

    queue_b = [start]
    visited_b = []
    out = []
    for x in inp:
        out.append([*x])

    for ix, x in enumerate(out):
        for iy, y in enumerate(x):
            if not [iy, ix] in visited:
                out[ix][iy] = '.'

    #direction style solution
    while len(queue_b) != 0:
        c = queue_b.pop(0)
        visited_b.append(c)
        n = [c[0], c[1]-1] if c[1]-1 >= 0 else None
        s = [c[0], c[1]+1] if c[1]+1 <= boundary_y else None
        w = [c[0]-1, c[1]] if c[0]-1 >= 0 else None
        e = [c[0]+1, c[1]] if c[0]+1 <= boundary_x else None
        sides = [n, s, w, e]

        if c in visited:
            c_dir = visited_dir[visited.index(c)][0]
            if sides[c_dir] and (not sides[c_dir] in visited_b) and (not sides[c_dir] in queue_b):
                queue_b.append(sides[c_dir])
                sides[c_dir] = None
            for x in visited_dir[visited.index(c)]:
                c_dir = directions[x]
                if sides[c_dir] and (not sides[c_dir] in visited_b) and (not sides[c_dir] in queue_b):
                    queue_b.append(sides[c_dir])
                    sides[c_dir] = None
        else:
            tile_counter += 1
            for x in sides:
                if x and (not x in visited_b) and (not x in queue_b):
                    queue_b.append(x)

    print('b:', tile_counter)

# 11
def day11(inp):
    inp = inp.split('\n')
    exp_cols = []
    exp_rows = []
    for ix, x in enumerate(inp):
        if len(set(x)) == 1:
            exp_rows.append(ix)
    for i in range(len(inp[0])):
        if len(set([x[i] for x in inp])) == 1:
            exp_cols.append(i)
    exp_cols.sort()
    exp_rows.sort()

    galaxies = []
    for ix, x in enumerate(inp):
        if x.find('#') != -1:
            for r in re.finditer('#', x):
                galaxies.append([r.start(), ix])
    a_sum = 0

    def expand(galaxy, mul=1):
        g = [galaxy[0], galaxy[1]]
        if exp_cols[0] < galaxy[0]:
            exp_c = 0
            for x in exp_cols:
                if x > galaxy[0]:
                    break
                exp_c += 1
            g[0] += exp_c * mul
            # part be replaces the column instead of adding to it
            if mul != 1:
                g[0] -= exp_c
        if exp_rows[0] < galaxy[1]:
            exp_r = 0
            for x in exp_rows:
                if x > galaxy[1]:
                    break
                exp_r += 1
            g[1] += exp_r * mul
            if mul != 1:
                g[1] -= exp_r
        return g

    b_galaxies = [expand(g, 1000000) for g in galaxies]
    galaxies = [expand(g) for g in galaxies]
    b_sum = 0

    for ig, g1 in enumerate(galaxies[:-1]):
        for ig2, g2 in enumerate(galaxies[ig:]):
            a_sum += abs(g1[0]-g2[0]) + abs(g1[1]-g2[1])
            b_sum += abs(b_galaxies[ig][0]-b_galaxies[ig+ig2][0]) + \
                     abs(b_galaxies[ig][1]-b_galaxies[ig+ig2][1])
    print('a:', a_sum)
    print('b:', b_sum)

# 12
def day12(inp):
    inp = inp.split('\n')

    def check_row(row, arrangement):
        until = row.find('?')
        if until == -1:
            r = row
        else:
            r = row[:until]
        r = r.replace('?', '.').split('.')
        while (r.count('')):
            r.remove('')
        if until == -1:
            if len(r) != len(arrangement):
                return False
            for ix, x in enumerate(r):
                if x.count('#') != arrangement[ix]:
                    return False
        else:
            for ix, x in enumerate(r):
                if ix >= len(arrangement) or x.count('#') > arrangement[ix]:
                    return False
        return True

    def solve_row(springs, arrangement):
        if springs.find('?') == -1:
            return check_row(springs, arrangement)
        s = []
        count = 0
        s.append(springs.replace('?', '.', 1))
        s.append(springs.replace('?', '#', 1))

        for x in s:
            if check_row(x, arrangement):
                count += solve_row(x, arrangement)
        return count

    a = 0
    for x in inp:
        tmp = x.split()
        a += solve_row(tmp[0], [int(x) for x in tmp[1].split(',')])
    print('a:', a)

if __name__ == "__main__":
    argpar = argparse.ArgumentParser()
    argpar.add_argument('-d', '--dummy', default=False, action='store_true', help='Use %day%.dummy input file')
    argpar.add_argument('day_num', type=int, help='The day of the challange')
    args = argpar.parse_args()
    try:
        inp = load_input(args.day_num, args.dummy)
    except FileNotFoundError:
        print('No file found', file=sys.stderr)
        exit(-1)

    try:
        locals()['day{}'.format(args.day_num)](inp)
    except KeyError:
        print('Day {} is not yet implemented'.format(args.day_num), file=sys.stderr)
