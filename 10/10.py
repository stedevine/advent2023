def get_start_position(lines):
    for r in range(0, len(lines)):
        for c in range(0, len(lines[0])):
            if lines[r][c] == 'S':
                return (r,c)

def get_next_step(r,c,lines):
    if r > 0 and lines[r-1][c] in ('|F7'):
        return (r-1,c, 'up')
    if r < len(lines) and lines[r+1] in ('|JL'):
        return (r+1,c, 'down')
    if c > 0 and lines[r][c-1] in ('-FL'):
        return (r, c-1, 'left')
    if c < len(lines[r]) and lines[r][c+1] in ('-J7'):
        return (r,c+1, 'right')
    
    print('error')
    
def part_1(lines):
    # find S
    # find one of the two pipes that connect S to the loop
    # follow the loop until we get back to S
    # result is number of steps taken // 2
    r,c = get_start_position(lines)
    print(f'{r}{c}')
    steps = 1
    r,c, direction = get_next_step(r,c,lines)
    #print(lines[r][c])
    while True:
        position = lines[r][c]
        if position == 'S':
            break
        #print(f'{steps} : {direction} {r},{c} {lines[r][c]}' )
        if direction == 'up':
            if position == '|':
                r -= 1
                direction = 'up'
            elif position == 'F':
                c += 1
                direction = 'right'
            else: # left
                c -= 1
                direction = 'left'

        elif direction == 'down':
            if position == '|':
                r += 1
                direction = 'down'
            elif position == 'J':
                c -= 1
                direction = 'left'
            else: # right
                c += 1
                direction = 'right'

        elif direction == 'right':
            if position == '7':
                r += 1
                direction = 'down'
            elif position == 'J':
                r -= 1
                direction  = 'up'
            else: # right
                c += 1
                direction = 'right'
        else: # 'left'
            if position == 'F':
                r += 1
                direction = 'down'
            elif position == 'L':
                r -= 1
                direction = 'up'
            else: # left
                c -= 1 
                direction = 'left' 
        
        steps += 1

    return (steps+1)//2


test1=""".....
.S-7.
.|.|.
.L-J.
....."""

test2="""..F7.
.FJ|.
SJ.L7
|F--J
LJ..."""

for t in [test1,test2]:
    r = part_1(t.split('\n'))
    print(f"test result {r}")

with open('./input.txt') as f:
    lines = f.readlines()
    print(f"part 1 result {part_1(lines)}")