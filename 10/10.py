def get_start_position(lines):
    for r in range(0, len(lines)):
        for c in range(0, len(lines[0])):
            if lines[r][c] == 'S':
                return (r,c)

def get_next_step(r,c,lines):
    if r > 0 and lines[r-1][c] in ('|F7'):
        return (r-1,c, 'U')
    if r < len(lines) and lines[r+1] in ('|JL'):
        return (r+1,c, 'D')
    if c > 0 and lines[r][c-1] in ('-FL'):
        return (r, c-1, 'L')
    if c < len(lines[r]) and lines[r][c+1] in ('-J7'):
        return (r,c+1, 'R')

# How do you make the arrows ↑ ↓ → ← on your keyboard? 
def part_1(lines):
    # find S
    # find one of the two pipes that connect S to the loop
    # follow the loop until we get back to S
    # result is number of steps taken // 2
    r,c = get_start_position(lines)
    print(f'start: ({r},{c})')
    steps = 1
    r,c, direction = get_next_step(r,c,lines)
    
    #print(f'first : {direction} : {lines[r][c]}')
    dp = direction + lines[r][c]
    while True:
        #print(f'dp: {dp} ({r},{c})') 
        #position = lines[r][c]
        if dp[-1] == 'S':
            break
        
        #dp = direction + position
        if   (dp == 'U|') : d = 'U'
        elif (dp == 'UF') : d = 'R'
        elif (dp == 'U7') : d = 'L'

        elif (dp == 'D|') : d = 'D'
        elif (dp == 'DJ') : d = 'L'
        elif (dp == 'DL') : d = 'R'

        elif (dp == 'L-') : d = 'L'
        elif (dp == 'LF') : d = 'D'
        elif (dp == 'LL') : d = 'U'

        elif (dp == 'R-') : d = 'R'
        elif (dp == 'R7') : d = 'D'
        else:               d = 'U'
        
        if      d == 'U':   r -=1
        elif    d == 'D':   r +=1
        elif    d == 'R':   c +=1
        else:               c -=1

        dp = d + lines[r][c]
        
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

for t in [test2]:
    r = part_1(t.split('\n'))
    print(f"test result {r}")

with open('./input.txt') as f:
    lines = f.readlines()
    print(f"part 1 result {part_1(lines)}")