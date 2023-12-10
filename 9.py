from load_input import load_day

dummy = 0
day = 9

if dummy:
    with open('{}.dummy'.format(day)) as f:
        inp = f.read()
else:
    inp = load_day(day)

inp = [[int(i) for i in x.split(' ')] for x in inp[:-1].split('\n')]
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
