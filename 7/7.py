
from operator import itemgetter
from collections import OrderedDict

def assemble_key(hand_map):
    # order the key by most common rank
    # then by A->2
    # then turn this into a hex number 
    sorted_by_count = OrderedDict(sorted(hand_map.items(), key=itemgetter(1), reverse=True))
    key = ""
    for k,v in sorted_by_count.items():
        key += (k*v)
    #print(key)
    #print(f'{hand_map} -> {key}')
    
    key = key.replace('T','a')
    key = key.replace('J','b')
    key = key.replace('Q','c')
    key = key.replace('K','d')
    key = key.replace('A','e')
    
    return int(key, 16)

def part_1(lines):
    sorted_hands = {}

    # group the hands into types
    types = {
        'five':[],
        'four':[],
        'full':[],
        'three':[],
        'two':[],
        'one':[],
        'high':[]
    }

    ranks = ['A','K', 'Q', 'J','T']
    ranks += [str(i) for i in range(9,1,-1)]
    def card_sort(item):
        return ranks.index(item)

    for line in lines:
        line=line.strip()
        hand = line.split(' ')[0]
        hand = sorted(hand,key=card_sort,reverse=False)
        line = ''.join(hand) + ' ' + line.split(' ')[1]
        hand_map = {}
        for c in hand:
            if c not in hand_map:
                hand_map[c] = 0
            hand_map[c] += 1

        v = list(hand_map.values())
        v.sort(reverse=True)
        #print(v)
        if v[0] == 5:
            types['five'].append((hand_map,line))
        elif v[0] == 4:
            types['four'].append((hand_map,line))
        elif v[0] == 3:
            if v[1] == 2:
                types['full'].append((hand_map,line))
            else:
                types['three'].append((hand_map,line))
        elif v[0] == 2:
            if v[1] == 2:
                types['two'].append((hand_map,line))
            else:
                types['one'].append((hand_map,line))
        else:
            types['high'].append((hand_map,line))
    
    xly = len(lines)
    result = 0
    for hand_type in ['five','four','full','three','two','one', 'high']:
        m = {}
        for l in types[hand_type]:
            #print(l)
            k = assemble_key(l[0])
            if k in m:
                m[k] += '*'
            else:
                m[k] = l[1]
        
        sorted_hands = OrderedDict(sorted(m.items(), reverse=True))
        print(hand_type)
        for h in sorted_hands.values():
            duplicates = 0
            v = h.split(' ')[1]
            if ('*' in v):
                duplicates = v.count('*')
                v = v[0:-duplicates]
            v = int(v)
            result += v * xly
            print(f'{h} -> {xly}')
            d = duplicates
            while d > 0:
                result += v * xly
                print(f'{h} -> {xly}')
                d -= 1
            xly -= 1
            xly -= duplicates
    
    return result

    # # sort the cards within each type
    # xly = 1
    # result = 0
    # for __loader__, hands in types.items():
    #     sorted_hands = {}
    #     for hand in hands:
    #         sorted_hands[assemble_key(hand[0])] = hand[1]

    #     sorted_hands = OrderedDict(sorted(sorted_hands.items()))
        
    #     for k,v in sorted_hands.items():
            
    #         print(f'{k} -> {v} * {xly}')
    #         result += int(v.split(' ')[1])*xly
    #         xly += 1

    # return result

test_3="""2345J 3
2345A 1
J345A 2
32T3K 5
Q2KJJ 13
T3T3J 17
KTJJT 34
KK677 7
T3Q33 11
T55J5 29
QQQJA 31
Q2Q2Q 19
2JJJJ 53
2AAAA 23
JJJJ2 41
JAAAA 43
AAAAJ 59
JJJJJ 37
AAAAA 61"""

test_2="""22222 5
KKKKK 5
88988 4
99992 4
9999J 4
JJKKK 3
QQKKK 3
KKQQQ 3
KKAAA 3
22298 3
222KQ 3
333KQ 3
2233J 2
22335 2
2233K 2
4455Q 2
5544J 2
22987 1
22Q87 1
33AKJ 1
33AQK 1
K9876 0
AJ234 0
QJ234 0"""

test="""32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483"""
for t in [test_3]:
    t1_result = part_1(t.split('\n'))
    print(f"result {t1_result}")


with open('./input.txt') as f:
    lines = f.readlines()
    #print(f"part 1 result {part_1(lines)}")