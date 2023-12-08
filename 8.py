from load_input import load_day
import math

dummy = 0
day = 8

if dummy:
    with open('{}.dummy'.format(day)) as f:
        inp = f.read()
else:
    inp = load_day(day)

inp = inp[:-1].split('\n\n')
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
