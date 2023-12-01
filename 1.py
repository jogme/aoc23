day = 1

from load_input import load_day

dummy = 0

if dummy:
    with open('{}.dummy'.format(day)) as f:
        inp = f.read()
else:
    inp = load_day(1)

inp = inp.split('\n')[:-1]

def first_num(x):
    for c in x:
        if c.isnumeric():
            return c

calib_val = 0
for x in inp:
    num = first_num(x)
    num += first_num(x[::-1])
    calib_val += int(num)

print('a: '+str(calib_val))

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

print('b: '+str(calib_val))
