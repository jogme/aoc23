from load_input import load_day
import re

dummy = 0
day = 3

if dummy:
    with open('{}.dummy'.format(day)) as f:
        inp = f.read()
else:
    inp = load_day(day)

inp = inp.split('\n')[:-1]
numbers = [list(filter(None, re.split(r'\D+', x))) for x in inp]
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
