from collections import namedtuple

def get_matches(line):
    line = line.strip()
    numbers = line.split(":")[1].strip()
    player = numbers.split("|")[0].strip().split(' ')
    player = [int(i) for i in player if i != '']
    winner = numbers.split("|")[1].strip().split(' ')
    winner = [int(i) for i in winner if i != '']
    return len(set(player) & set(winner))

def part_1(lines):
    result = 0 
    for line in lines:
        matches  = get_matches(line)
        if matches > 0: 
            result += 2 ** (matches-1)
        #print(set(player)&set(winner))
        #print(winner)
    return result

# slow
# def part_2(lines):
#     map = {}
#     for i in range(1,len(lines)+1):
#         map[i] = 1
    
#     for line in lines:
#         line = line.strip()
#         card_number = int(line.split('Card ')[1].split(':')[0])
#         for _ in range(0,map[card_number]):
#             matches  = get_matches(line)
#             if matches > 0:
#                 for i in range(card_number+1, min(card_number+1+matches, len(lines)+1)):
#                     map[i] += 1
#         print(f'{card_number} : {matches}')

#     return sum(list(map.values()))

def part_2(lines):
    results = {}
    for line in lines:
        line = line.strip()
        card_number = int(line.split('Card ')[1].split(':')[0])
        results[card_number] = (get_matches(line),1)

    for card_number, r in results.items():
        if r[0] > 0:
            for i in range(card_number+1, min(card_number+1+r[0], len(lines)+1)):
                o = results[i]
                results[i] = (o[0], o[1]+r[1])
        
    return sum([i[1] for i in list(results.values())])

test="""Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""

test1_result = part_1(test.split('\n'))
print(f"test 1 result {test1_result}")

test2_result = part_2(test.split('\n'))
print(f"test 2 result {test2_result}")

with open('./input.txt') as f:
    lines = f.readlines()

    print(f"part 1 result {part_1(lines)}")
    print(f"part 2 result {part_2(lines)}")