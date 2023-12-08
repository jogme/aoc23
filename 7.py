from load_input import load_day
from functools import cmp_to_key

dummy = 0
day = 7

if dummy:
    with open('{}.dummy'.format(day)) as f:
        inp = f.read()
else:
    inp = load_day(day)

inp = inp[:-1].split()
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
