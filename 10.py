from load_input import load_day

dummy = 0
day = 10

if dummy:
    with open('{}.dummy'.format(day)) as f:
        inp = f.read()
else:
    inp = load_day(day)

inp = inp[:-1].split('\n')

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
for ix,x in enumerate(inp):
    tmp = x.find('S')
    if tmp != -1:
        start.append(tmp)
        start.append(ix)
        break

boundary_x = len(inp[0]) - 1
boundary_y = len(inp) - 1

queue = [start]
visited = []

while True:
    c = queue.pop(0)
    visited.append(c)
    x = c[0]
    y = c[1]
    # WEST
    if x != 0 and not [x-1, y] in visited and \
        is_valid(inp[y][x], inp[y][x-1], WEST):
            queue.append([x-1, y])
    # EAST
    elif x < boundary_x and not [x+1, y] in visited and \
        is_valid(inp[y][x], inp[y][x+1], EAST):
            queue.append([x+1, y])
    # NORTH
    elif y != 0 and not [x, y-1] in visited and \
        is_valid(inp[y][x], inp[y-1][x], NORTH):
            queue.append([x, y-1])
    # SOUTH
    elif y < boundary_y and not [x, y+1] in visited and \
        is_valid(inp[y][x], inp[y+1][x], SOUTH):
            queue.append([x, y+1])
    if len(queue) == 0:
        break

print('a:', int(len(visited)/2))
