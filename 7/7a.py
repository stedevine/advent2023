def part_1(lines):
    # group the hands into types
    types = {
        'high':[],
        'one':[],
        'two':[],
        'three':[],
        'full':[],
        'four':[],
        'five':[]
    }
    ranks = ['A','K', 'Q', 'J','T']
    ranks += [str(i) for i in range(9,1,-1)]
    def card_sort(item):
        return ranks.index(item)

    for line in lines:
        line=line.strip()
        #hand = line.split(' ')[0]
        #hand = sorted(hand,key=card_sort)
        #line = ''.join(hand) + ' ' + line.split(' ')[1]
        hand_map = {}
        for c in line.split(' ')[0]:
            if c not in hand_map:
                hand_map[c] = 0
            hand_map[c] += 1

        v = list(hand_map.values())
        v.sort(reverse=True)
        #print(v)
        if v[0] == 5:
            types['five'].append(line)
        elif v[0] == 4:
            types['four'].append(line)
        elif v[0] == 3:
            if v[1] == 2:
                types['full'].append(line)
            else:
                types['three'].append(line)
        elif v[0] == 2:
            if v[1] == 2:
                types['two'].append(line)
            else:
                types['one'].append(line)
        else:
            types['high'].append(line)
    """    
    custom_alphabet_order = {
        'A': 0, 'K': 1, 'Q': 2, 'J': 3, 'T': 4, 
        '9': 5, '8': 6, '7': 7, '6': 8, '5': 9, 
        '4': 10,'3': 11, '2': 12, '1':13, '0':14, ' ':15}
    
    def hand_sort(word):
        return [custom_alphabet_order[char] for char in word]
    """

    result = 0
    """
    xly = len(lines)
    for k,v in types.items():
        s = sorted(v, key=hand_sort)
        #print(f'{k} {s}')
        for h in s:
            v = int(h.split(' ')[1])
            result += v*xly
            print(f'{h} {v}*{xly} {v*xly}')
            xly -= 1
    """
    return result


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
for t in [test, test_2]:
    t1_result = part_1(t.split('\n'))
    print(f"result {t1_result}")

with open('./input.txt') as f:
    lines = f.readlines()
    print(f"part 1 result {part_1(lines)}")