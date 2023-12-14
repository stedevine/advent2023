from functools import reduce
def parse_input_into_multiple_games(lines):
    def parse_line(line):
        v = line.split(":")[1].split(" ")        
        return [int(t) for t in v if t != '']

    times = parse_line(lines[0])
    dist = parse_line(lines[1])
    return (times,dist)

def parse_input_into_single_game(lines):
    def parse_line(line):
        v = line.split(":")[1].replace(" ","")       
        return int(v)

    times = parse_line(lines[0])
    dist = parse_line(lines[1])
    return (times,dist)

def part_1(lines):
    result = parse_input_into_multiple_games(lines)
    to_multiply = []
    for i in range(0,len(result[0])):
        t = result[0][i]
        d = result[1][i]
        ways_to_win = 0
        for i in range(1, t):
            moved = i * (t - i)
            if moved > d:
                ways_to_win += 1
        if ways_to_win > 0:
            to_multiply.append(ways_to_win)
    return reduce(lambda x, y: x*y,to_multiply)

def part_2(lines):
    time, distance = parse_input_into_single_game(lines)
    # go forward until we beat
    s = 1
    while True:
        moved = s * (time - s)
        if moved > distance:
            break
        s += 1
    #print(t)

    # go backwards until we don't beat
    e = time
    while True:
        moved = e * (time - e)
        if moved > distance:
            break
        e -= 1

    #print(f"{s} {e} ({e-s+1})")
    return e - s + 1

test="""Time:      7  15   30
Distance:  9  40  200"""
test1_result = part_1(test.split('\n'))
print(f"test 1 result {test1_result}")

test2_result = part_2(test.split('\n'))
print(f"test 1 result {test2_result}")

with open('./input.txt') as f:
    lines = f.readlines()
    print(f"part 1 result {part_1(lines)}")
    print(f"part 2 result {part_2(lines)}")