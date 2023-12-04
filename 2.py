from load_input import load_day
import numpy

dummy = 0
day = 2

if dummy:
    with open('{}.dummy'.format(day)) as f:
        inp = f.read()
else:
    inp = load_day(day)

possible = {'red':12, 'green':13, 'blue':14}
counting = 0
power = 0

inp = [x.split(': ')[1].split('; ') for x in inp.split('\n')[:-1]]

def is_count(dic):
    for x in possible.keys():
        if x not in dic or possible[x] < dic[x]:
            return False
    return True

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
