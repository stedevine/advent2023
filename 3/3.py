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
            # Let's work out what *number* this is - move right until we hit the end of the row or a non-digit value

            if cursor.isdigit():
                left = c
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
                right = c - 1

                # We have the number and its position (the row it lives on and the columns where it starts and ends)
                # Check around the number to see if we should count it
                if check_around(r, left, right, lines):
                    result += num
            c += 1
        r += 1    
    return result

def get_number(row, col, lines, number_map):
    c = col
    while c >=0 and lines[row][c].isdigit():
        c -= 1

    c +=  1
    cursor = lines[row][c]
    num = int(cursor)
    c += 1
    cursor = lines[row][c]
    while c < len(lines[row]) and cursor.isdigit():
        num = num*10
        num += int(cursor)
        c += 1
        if c == len(lines[row]):
            break
        cursor = lines[row][c]
    # explore left to get the start of the number
    # then right to get the end
    
    # store the number and its co-ord
    number_map[f'{row},{c}'] =  num

def find_numbers(row, col, lines):
    check_left = col > 0
    check_right = col < (len(lines[row]) - 1)
    check_above = row > 0
    check_below = row < (len(lines) - 1)

    number_map = {}

    if check_left and lines[row][col-1].isdigit():
        get_number(row,col-1,lines, number_map)

    if check_right and lines[row][col+1].isdigit():
        get_number(row,col+1,lines, number_map)

    if check_above:
        if lines[row-1][col].isdigit():
            get_number(row-1,col,lines, number_map)
        if check_left and lines[row-1][col-1].isdigit():
            get_number(row-1,col-1,lines, number_map)
        if check_right and lines[row-1][col+1].isdigit():
            get_number(row-1,col+1,lines, number_map)


    if check_below:
        if lines[row+1][col].isdigit():
            get_number(row+1,col,lines, number_map)
        if check_left and lines[row+1][col-1].isdigit():
            get_number(row+1,col-1,lines, number_map)
        if check_right and lines[row+1][col+1].isdigit():
            get_number(row+1,col+1,lines, number_map)

    return number_map


def part_2(lines):
    result = 0

    r = 0 
    while r < len(lines):
        c = 0
        while c < len(lines[r]):
            
            cursor = lines[r][c]

            if cursor == '*':
                # find the numbers around the *
                map = find_numbers(r,c,lines)
                if len(map) == 2:
                    result += list(map.values())[0] * list(map.values())[1]
            c += 1
        r += 1 

    return result
    print('----')

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

test2_result = part_2(test.split('\n'))
print(f"test 2 result {test2_result}")


with open('./input.txt') as f:
    lines = f.readlines()
    print(f"part 1 result {part_1(lines)}")
    print(f"part 2 result {part_2(lines)}")