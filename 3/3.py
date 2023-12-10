def check_around(row, left, right, lines):
    
    symbols = '#$%&*+-/=@'


    check_left = left > 0
    check_right = right < (len(lines[row]) - 1)
    check_above = row > 0
    check_below = row < (len(lines) - 1)

    if check_left and lines[row][left-1] in symbols:
        return True

    if check_right and lines[row][right+1] in symbols:
        return True

    if check_above:
        for c in range(left, right+1):
            if lines[row-1][c] in symbols:
                return True
        if check_left and lines[row-1][left-1] in symbols:
            return True
        if check_right and lines[row-1][right+1] in symbols:
            return True

    if check_below:
        for c in range(left, right+1):
            if lines[row+1][c]in symbols:
                return True
        if check_left and lines[row+1][left-1] in symbols:
            return True
        if check_right and lines[row+1][right+1] in symbols:
            return True
    
    return False



def part_1(lines):
    result = 0

    r = 0 
    while r < len(lines):
        c = 0
        while c < len(lines[r]):
            
            cursor = lines[r][c]

            # If we've landed on a digit 
            # determine what the number is (move right until we hit the end of the row or a non-digit value)
            # determine if it should be counted - look at the values "around" the number - check if they contain a symbol (non-digit, non-dot) character
            if cursor.isdigit():
                l_index = c
                num = int(cursor)
                c += 1
                cursor = lines[r][c]
                while c < len(lines[r]) and cursor.isdigit():
                    num = num*10
                    num += int(cursor)
                    c += 1
                    if c == len(lines[r]):
                        break
                    cursor = lines[r][c]
                r_index = c - 1
                #print(f"{num}  row:{r} cols: {l_index} {r_index}")

                # We have the number, the left and right position and the row it lives on.
            
                # Check around the number:
                if check_around(r, l_index, r_index, lines):
                    #print(f"{num}  row:{r} cols: {l_index} {r_index}")
                    result += num



            #for c in range(0, len(lines[r])):
            #l += lines[r][c]
            c += 1
        r += 1    
        #print(l)
    
    #print('--')
    #print(result)
    return result
    #print(len(lines))
    #for line in lines:
    #    print(len(line))

test="""467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""

test1_result = part_1(test.split('\n'))
print(f"test 1 result {test1_result}")

with open('./input.txt') as f:
    a = set()
    lines = f.readlines()
    for l in lines:
        for c in l:
            a.add(c)

    b = list(a)
    b.sort()
    print(b)


    print(f"part 1 result {part_1(lines)}")