from load_input import load_day

dummy = 0
day = 5

if dummy:
    with open('{}.dummy'.format(day)) as f:
        inp = f.read()
else:
    inp = load_day(day)

inp = inp[:-1].split('\n\n')
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
