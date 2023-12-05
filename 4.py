from load_input import load_day

dummy = 0
day = 4

if dummy:
    with open('{}.dummy'.format(day)) as f:
        inp = f.read()
else:
    inp = load_day(day)

inp = [x.split(': ')[1].split(' | ') for x in inp.split('\n')[:-1]]
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
