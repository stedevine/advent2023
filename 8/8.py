from collections import deque
from math import gcd 
def get_pos(value, instruction):
    # instruction is L or R
    # value is of the form ; (BBB, CCC)
    if instruction == 'L':
        return value.split(',')[0][1:]

    return value.split(',')[1].strip()[:-1]

def enque(lines):
    inst = lines[0].strip()
    q = deque(maxlen=len(inst))
    for i in inst:
        q.append(i)
    
    return q

def get_map(lines):
    map = {}
    for i in range(2, len(lines)):
        key = lines[i].split('=')[0].strip()
        value = lines[i].split('=')[1].strip()
        #print(f'{k} -> {v}')
        map[key] = value 
    
    return map

def part_1(lines):
    q = enque(lines)
    map = get_map(lines)
    
    # start at AAA
    pos = 'AAA'
    steps = 0
    while True:
        i = q.popleft()
        q.append(i)
        steps += 1
        pos = get_pos(map[pos], i)
        if pos == 'ZZZ' and steps % len(q) == 0:
            break

    return steps

def part_2(lines):
    q = enque(lines)
    map = get_map(lines)

    positions = list(filter(lambda a: a[-1] == 'A', map.keys()))
    pos_count = []
    for position in positions:
        steps = 0
        pos = position
        while True:
            i = q.popleft()
            q.append(i)
            #print(i)
            steps += 1
            pos = get_pos(map[pos], i)
            if pos[-1] == 'Z' and steps % len(q) == 0:
                #print(f"{position} : {steps}")
                pos_count.append(steps)
                break
            
    lcm = 1
    for i in pos_count:
        lcm = lcm*i//gcd(lcm, i)

    return lcm


test="""RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)"""

test2="""LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)"""

for t in [test, test2]:
    r = part_1(t.split('\n'))
    print(f"test result {r}")

with open('./input.txt') as f:
    lines = f.readlines()
    print(f"part 1 result {part_1(lines)}")

test_part_2="""LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)"""


r = part_2(test_part_2.split('\n'))
print(f"test result 2 {r}")

with open('./input.txt') as f:
    lines = f.readlines()
    print(f"part 2 result {part_2(lines)}")