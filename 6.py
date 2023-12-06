from load_input import load_day

dummy = 0
day = 6

if dummy:
    with open('{}.dummy'.format(day)) as f:
        inp = f.read()
else:
    inp = load_day(day)

inp = [[int(i) for i in x.split(': ')[1].split()] for x in inp[:-1].split('\n')]

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
